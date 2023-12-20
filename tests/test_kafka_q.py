import pytest, os, time, random
from src.q.kafka_q import kafka_q
from datetime import datetime as dt
from src.utils.pfs_logging import log


class TestKQ:
    messages = [
        { "greeting": "hello world"},
        {}, #empty!
        { 
            "type" : "two levels",
            "level1": {
                "msg":"level 1 message"
            },
            "level2": {
                "msg":"level 2 message"
            }
        },
        {
            "type" : "number",
            "value": 100
        },
        {
            "type": "arrays",
            "strs": ["aaa", "bbb", "ccc"],
            "nums": [1,2,3],
            "void": [],
            "bools": [True, True, False]
        }
    ]

    # using new topic with every test run
    # so regardless of Kafka config, we dont
    # mess up the order of messages with previous
    # test runs!
    new_topic = dt.timestamp(dt.now())
    _topics = [f'Q1-{new_topic}', f'Q2-{new_topic}']
    # topics = [NewTopic(t,1,1) for t in _topics]

    # # admin client
    # admin = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
    # admin.create_topics(topics)

    # set env for ping
    os.environ["PFS_KAFKA_SRVR"] = 'localhost'
    os.environ["PFS_KAFKA_PORT"] = '9092'
    os.environ["PFS_KAFKA_RQ"] = _topics[0]
    os.environ["PFS_KAFKA_WQ"] = _topics[1]
    ping = kafka_q()
    log.debug(f"ping topics:{ping.consumer.topics()}")

    # reverse the queue for pong
    os.environ["PFS_KAFKA_RQ"] = _topics[1]
    os.environ["PFS_KAFKA_WQ"] = _topics[0]
    pong = kafka_q()
    log.debug(f"pong topics:{pong.consumer.topics()}")


    def flush(self):
        """Flushing the content of the queue before the testing
        """
        self.ping.producer.flush()
        self.pong.producer.flush()
        log.debug(self.pong.get_status())
        log.debug(self.ping.get_status())


    def long_message(self, size=1000):
        ascii = list(range(33,127)) #printable ascii characters
        return {"msg":"".join([chr(ascii[random.randrange(len(ascii))]) for i in range(size)])}
            

    @pytest.mark.parametrize("msg", messages)
    @pytest.mark.parametrize("count", [1,5,10])
    def test_ping_pong(self, msg, count):
        self.flush()
        for i in range(count):
            msg["sendTime"] = dt.timestamp(dt.now())
            assert(self.ping.write(msg,block=True))
            # time.sleep(30) # allow 30 seconds for the message to propagate
            msg2 = self.pong.read()
            assert msg == msg2



    @pytest.mark.parametrize("msg", messages)
    @pytest.mark.parametrize("count", [1,100,1000])
    def test_bulk_ping_pong(self, count, msg):
        self.flush()
        items = [{str(i):msg} for i in range (count)]
        assert self.ping.bulk_write(items)
        time.sleep(10) # allow 30 seconds for the message to propagate
        items2 = self.pong.bulk_read(max_items=count)
        for i in items:
            assert i in items2


    @pytest.mark.parametrize("size", [10000, 100000])
    def test_long_messages(self, size):
        self.flush()
        msg = self.long_message(size)
        self.test_ping_pong(msg=msg,count=1)
        self.test_bulk_ping_pong(count=1, msg=msg)
