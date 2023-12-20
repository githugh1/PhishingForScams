from kafka import KafkaConsumer, KafkaProducer, KafkaClient
import time, sys, os, json
from src.utils.pfs_logging import log
from src.q.queue import queue, QException
from kafka.producer.record_accumulator import AtomicInteger

PRODUCER_CLIENT_ID_SEQUENCE = AtomicInteger()
CONSUMER_CLIENT_ID_SEQUENCE = AtomicInteger()

class kafka_q(queue):
    """This class implements a queue using Kafka. It is deriving :class:`src.q.queue`.

    The following environement variables must be set prior to initialising this class
        `PFS_KAFKA_SRVR` : kafka server ip address or dns
        `PFS_KAFKA_PORT` : kafka server port
        `PFS_KAFKA_RQ` : name of the queue (topic) to read from
        `PFS_KAFKA_WQ` : name of the queue (topic) to write to

    :param producer: A handle to :class:`kafka.KafkaProducer`
    :type producer: class:`kafka.KafkaProducer`
    ...
    :param consumer: A handle to :class:`kafka.KafkaConsumer`
    :type consumer: class:`kafka.KafkaConsumer`
    ...
    :param kafka_config: config dict containing kafka particulars:
        {
            server: <server ip or dns>
            port: <port>
            rtopic: <queue topic> to read from
            wtopic: <queue topic> to write to
        }
    :type kafka_config: dict
    ...
    :raises QException: when errors occur (TODO: need to define this clearer!)
    """

    def __init__(self):
        """class constructor

        The following environement variables must be set:
        `PFS_KAFKA_SRVR` : kafka server ip address or dns
        `PFS_KAFKA_PORT` : kafka server port
        `PFS_KAFKA_RQ` : name of the queue (topic) to read from
        `PFS_KAFKA_WQ` : name of the queue (topic) to write to

        """

        # env keys
        keys = [
            "PFS_KAFKA_SRVR",
            "PFS_KAFKA_PORT",
            "PFS_KAFKA_RQ",
            "PFS_KAFKA_WQ"
        ]

        for k in keys:
            if k not in os.environ:
                raise QException(f"{__class__}: environement variable {k} is undefined")

        self.config = {
            "server": os.getenv("PFS_KAFKA_SRVR", "localhost"),
            "port": os.getenv("PFS_KAFKA_PORT", "9092"),
            "rtopic": os.getenv("PFS_KAFKA_RQ"),
            "wtopic": os.getenv("PFS_KAFKA_WQ"),
            "request_timeout": os.getenv("PFS_KAFKA_REQUEST_TIMEOUT_MS", "3000"),
            "consumer_id": os.getenv("PFS_KAFKA_COMSUMER_ID", "PFS_CONSUMER"),
            "consumer_group_id": os.getenv("PFS_KAFKA_COMSUMER_GROUP_ID", "PFS_CONSUMER_GROUP"),
            "producer_id": os.getenv("PFS_KAFKA_PRODUCER_ID", "PFS_PRODUCER"),
        }

        # initializing Kafka producer (threading safe)
        id = PRODUCER_CLIENT_ID_SEQUENCE.increment()
        self.producer = KafkaProducer(bootstrap_servers=[f"{self.config['server']}:{self.config['port']}"],
                                      #request_timeout_ms=int(self.config['request_timeout']),
                                      value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                      client_id=f"{self.config['producer_id']}-{id}")

        # initializing Kafka consumer (not treading safe!)
        id = CONSUMER_CLIENT_ID_SEQUENCE.increment()
        self.consumer = KafkaConsumer(bootstrap_servers=[f"{self.config['server']}:{self.config['port']}"],
                                      value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                      #request_timeout_ms=int(self.config['request_timeout']),
                                      #consumer_timeout_ms=3000,
                                      enable_auto_commit=True, auto_offset_reset='earliest',
                                      client_id=f"{self.config['consumer_id']}-{id}",
                                      group_id=f"{self.config['consumer_group_id']}-{id}")
        
        self.consumer.subscribe([self.config["rtopic"]])


    def get_consumer_status(self):
        con = self.consumer
        status = {
                "client_id": con.config['client_id'],
                "subscription": con.subscription(),
                "inflight fetches": con._fetcher.in_flight_fetches(),
                "topics": con._client._topics,
                "cluster topics": con._client.cluster.topics(),
                "topic partitions": con.assignment()
            }
        log.debug(f"consumer status: {status}")
        return status
    
    def get_producer_status(self):
        prod = self.producer
        result = prod._sender._accumulator.ready(prod._sender._metadata)
        ready_nodes, next_ready_check_delay, unknown_leaders_exist = result
        rn = []
        for node in list(ready_nodes):
            rn.append({"node_id" : node, "ready": prod._sender._client.is_ready(node)})

        status = {
                "client_id": self.producer.config['client_id'],
                "has unsent": self.producer._accumulator.has_unsent(),
                "inflight requests": self.producer._sender._client.in_flight_request_count(),
                "ready_nodes": rn
            }
        log.debug(f"producer status: {status}")
        return status

    def get_status(self):
        status = {
            "producer" : self.get_producer_status(),
            "consumer" : self.get_consumer_status()
        }
        return status

 
    def read(self):
        """Returns an item from kafka queue (topic). This method will block for synchronous retrival of the item.
        :return: An item from the queue as a UTF-8 decoded string
        :rtype: string
        """
        log.debug(f"{self.consumer.config['client_id']} topics:{self.consumer.topics()}")
        # msg = self.bulk_read(1)[0]
        # msg = self.consumer.__next__()
        msg = self.consumer.poll(timeout_ms=5000, max_records=1)
        if not msg or len(msg) == 0:
            log.error(f"message was empty!{msg}")
            return msg
        
        key, value = msg.popitem()
        log.debug(f"recieved msg:{value[0].value}")
        return value[0].value

    def bulk_read(self, max_items: int = 500) -> list:
        """Returns a list of items from kafka queue (topic). Similar to read but returns a list upto max_items
        This method will block for synchronous retrival of the items.
        
        Arguments:
            max_items (int, optional): The maximum number of items returned
                in a single call to :meth:`~kafka.KafkaConsumer.poll`.
                Default: 500

        Returns:
            [dict]: a list of items from the queue as a list of dicts
        """

        while True:
            try: 
                # return {TopicPartition: [messages]}
                # self.consumer.config["max_poll_records"] = max_items
                msg = self.consumer.poll(timeout_ms=5000, max_records=max_items)
                print(f"\n\n\nMSG:\n{msg}\n\n")
                if not msg or len(msg) == 0:
                    log.error(f"message was empty!{msg}")
                    return msg
                
                key, values = msg.popitem()
                return [i.value for i in values]

            except:
                # Handle any exception here
                continue

    
    def write(self, item: dict, block: bool = False) -> bool:
        '''Writes an item to kafka queue(topic). The queue (topic) should be assigned during init

        Arguments:
            item (dict): a dict item to be sent over kafka
            block (bool, optional): blocks for synchronous sending if true
                               (timeout after PFS_Q_SEND_TIMEOUT seconds, default 30)
        
        Returns:
            bool: True if succeeded or False if failed.
        '''
        if type(item) != dict:
            log.info(f"item is of type {type(item)} and is not dict")
            return False
        
        msg_sent = False
        def on_success(record_mdata):
            print(
                    f"""
                    wrote message successfully:\n\t
                    topic:{record_mdata.topic}\n\t
                    partition:{record_mdata.partition}\n\t
                    offset:{record_mdata.offset}
                    """
                )
            nonlocal msg_sent
            msg_sent = True
            

        def on_error(error):
            log.error("error in writing to kafka", exc_info=1)

        # retruns FutureRecordMetadata
        record = self.producer.send(self.config["wtopic"], item). \
                            add_callback(on_success).add_errback(on_error)
        # if block:
        #     try:
        #         record.get(timeout=int(self.config["request_timeout"]))
        #         self.producer.flush()
        #     except KafkaError as e:
        #         log.error('synchronous sending failed')
        #         on_error(e)

        while block and not msg_sent:
            log.debug('waiting for synchronous sending')
            log.debug(f'msg_sent = {msg_sent}')
            log.debug(f'record.succeeded = {record.succeeded()}')
            time.sleep(1) # wait for the message to send!
        
        log.debug(f'msg_sent = {msg_sent}')
        return not block or record.succeeded()

    def bulk_write(self, items):
        '''Writes a list of items to kafka queue(topic). The queue (topic) should be assigned during init.
           This is only async sending event

           Arguments:
               items (list(dict)): a list of dict items to be sent over kafka
        
           Returns:
               bool: True if succeeded or False if failed.
        '''
        if type(items) != list :
            log.info(f"items is of type {type(items)} and is not list")
            return False
        
        result = True

        for i in items:
            result = result and self.write(i, block=False)
            if not result:
                break
        
        return result
        
        

        