import pytest
import os
import time
import random
from src.q.kafka_q import kafka_q
from datetime import datetime as dt
from src.utils.pfs_logging import log


class TestKQ:
    ''' A testing class for {py:class}`src.q.kafka_q`
    '''
    messages: list[dict] = [
        {"greeting": "hello world"},
        {},  # empty!
        {
            "type": "two levels",
            "level1": {
                "msg": "level 1 message"
            },
            "level2": {
                "msg": "level 2 message"
            }
        },
        {
            "type": "number",
            "value": 100
        },
        {
            "type": "arrays",
            "strs": ["aaa", "bbb", "ccc"],
            "nums": [1, 2, 3],
            "void": [],
            "bools": [True, True, False]
        }
    ]
    '''
        various test messages
    '''

    # using new topic with every test run
    # so regardless of Kafka config, we dont
    # mess up the order of messages with previous
    # test runs!
    _new_topic = dt.timestamp(dt.now())
    _topics = [f'Q1-{_new_topic}', f'Q2-{_new_topic}']
    # topics = [NewTopic(t,1,1) for t in _topics]

    # # admin client
    # admin = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
    # admin.create_topics(topics)

    # set env for ping
    os.environ["PFS_KAFKA_SRVR"] = 'localhost'
    os.environ["PFS_KAFKA_PORT"] = '9092'
    os.environ["PFS_KAFKA_RQ"] = _topics[0]
    os.environ["PFS_KAFKA_WQ"] = _topics[1]
    ping: kafka_q = kafka_q()
    ''' forward sending kafka_q

        {envvar}`PFS_KAFKA_RQ` {math}`\hspace{10pt} \overrightarrow{process\\ and\\ send\\ to} \hspace{10pt}` {envvar}`PFS_KAFKA_WQ`
    '''
    log.debug(f"ping topics:{ping.consumer.topics()}")

    # reverse the queue for pong
    os.environ["PFS_KAFKA_RQ"] = _topics[1]
    os.environ["PFS_KAFKA_WQ"] = _topics[0]
    pong: kafka_q = kafka_q()
    ''' backward sending kafka_q

        {envvar}`PFS_KAFKA_WQ` {math}`\hspace{10pt} \overrightarrow{process\\ and\\ send\\ to} \hspace{10pt}` {envvar}`PFS_KAFKA_RQ`
    '''
    log.debug(f"pong topics:{pong.consumer.topics()}")

    def flush(self):
        """Flushing the content of the queue before the testing
        """
        self.ping.producer.flush()
        self.pong.producer.flush()
        log.debug(self.pong.get_status())
        log.debug(self.ping.get_status())

    def long_message(self, size:int =1000) -> dict:
        ''' creates a random long message

            the message contains random letters upto the specified size

            :param int size: the number of letters in the message (default: 1000)
            :returns: a dict a key _'msg'_ containing a long message 
        '''
        ascii = list(range(33, 127))  # printable ascii characters
        return {"msg": "".join([chr(ascii[random.randrange(len(ascii))])
                                for i in range(size)])}

    @pytest.mark.parametrize("msg", messages)
    @pytest.mark.parametrize("count", [1, 5, 10])
    def test_ping_pong(self, msg: dict, count: int) -> None:
        ''' checks the consistency of {py:class}`kafka_q` messaging

            {py:data}`ping` and {py:data}`pong` topics are reveresed by design.
            This function sends a message to ping using {py:meth}`src.q.kafka_q.kafka_q.write`
            then reads it back from pong using {py:meth}`src.q.kafka_q.kafka_q.read` and
            checks if it is consistent with the original message.

            :param dict msg: a message to send through ping pong
            :param int count: the number of times to repeat the check

        '''
        self.flush()
        for i in range(count):
            msg["sendTime"] = dt.timestamp(dt.now())
            assert (self.ping.write(msg, block=True))
            # time.sleep(30) # allow 30 seconds for the message to propagate
            msg2 = self.pong.read()
            assert msg == msg2

    @pytest.mark.parametrize("msg", messages)
    @pytest.mark.parametrize("count", [1, 100, 1000])
    def test_bulk_ping_pong(self, count: int, msg: dict) -> None:
        ''' checks the consistency of {py:class}`kafka_q` bulk messaging

            {py:data}`ping` and {py:data}`pong` topics are reveresed by design.
            This function sends bulk messages to ping using {py:meth}`src.q.kafka_q.kafka_q.bulk_write`
            then reads them back from pong using {py:meth}`src.q.kafka_q.kafka_q.bulk_read` and
            checks if they are consistent with the original messages.

            :param dict msg: a message to send through ping pong
            :param int count: the number messages in each bulk send/recieve

            :::{note}
            unlike {py:meth}`test_ping_pong`, the message is replicated multiple
            times to create an array of items to send in bulk.
            ::: 

        '''
        self.flush()
        items = [{str(i): msg} for i in range(count)]
        assert self.ping.bulk_write(items)
        time.sleep(10)  # allow 30 seconds for the message to propagate
        items2 = self.pong.bulk_read(max_items=count)
        for i in items:
            assert i in items2

    @pytest.mark.parametrize("size", [10000, 100000])
    def test_long_messages(self, size: int) -> None:
        ''' tests the send and recieve of a long message

            It genereates a {py:meth}`long_message` and tests
            using read/write and bulk_read/bulk_write

            :param int size: the size of the long message
        '''
        self.flush()
        msg = self.long_message(size)
        self.test_ping_pong(msg=msg, count=1)
        self.test_bulk_ping_pong(count=1, msg=msg)
