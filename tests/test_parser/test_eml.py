import json, pytest
import os
from src.q.kafka_q import kafka_q
from datetime import datetime as dt
from src.utils.pfs_logging import log
from src.parser.email_parser import EmailParser
from .expected_outputs import EXPECTED_EML_1, EXPECTED_EML_2, EXPECTED_EML_3, EXPECTED_EML_4, EXPECTED_EML_5, EXPECTED_EML_6

CONFIG = {
    'host': 'localhost', # Sub with IP address in future servers
    'user': 'root', # Could change with additional users
    'password': 'your_password',
    'database': 'phishing_for_scams', 
    'port': '3306',
    'raise_on_warnings': True
}

# include filepaths and expected outputs for testing purposes

FILES = ['tests/data/example1.eml', 'tests/data/example2.eml', 'tests/data/example3.eml', 'tests/data/example4.eml', 'tests/data/example5.eml', 'tests/data/example6.eml']
OUTPUTS = [EXPECTED_EML_1, EXPECTED_EML_2, EXPECTED_EML_3, EXPECTED_EML_4, EXPECTED_EML_5, EXPECTED_EML_6]

class TestParser:

    # setup

    @pytest.fixture
    def email_parser(self):
        return EmailParser(CONFIG)
    
    @pytest.fixture
    def parsed_email(self, email_parser):
        parsed = []

        for file in FILES:
            decoded = email_parser.parse_email(file)
            parsed.append(json.loads(decoded))

        return parsed

    # tests parser output

    keys = set().union(*(d.keys() for d in OUTPUTS))

    @pytest.mark.parametrize("index", range(len(FILES)))
    @pytest.mark.parametrize("key", keys)
    def test_parse_email_keys(self, parsed_email, index, key):
        eml = parsed_email[index]
        output = OUTPUTS[index]

        if key in output:
            assert key in eml, f"Parsed email missing key: {key}"
            assert eml[key] == output[key], f"Key values do not match for key: {key}"

    @pytest.mark.parametrize("index", range(len(FILES)))
    def test_parse_email(self, parsed_email, index):
        eml = parsed_email[index]
        output = OUTPUTS[index]
        assert eml == output, "Parsed email does not match expected output - Check Formatting"

    # tests parser can send through kafka

    _new_topic = dt.timestamp(dt.now())
    _topics = [f'Q1-{_new_topic}', f'Q2-{_new_topic}']

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

    @pytest.mark.parametrize("count", [1, 2, 3])
    def test_parser_ping_pong(self, parsed_email: list[dict], count: int) -> None:
        ''' checks the consistency of {py:class}`kafka_q` messaging

            {py:data}`ping` and {py:data}`pong` topics are reveresed by design.
            This function sends a parsed email to ping using {py:meth}`src.q.kafka_q.kafka_q.write`
            then reads it back from pong using {py:meth}`src.q.kafka_q.kafka_q.read` and
            checks if it is consistent with the original parsed message.

            :param list[dict] parsed_email: a message to send through ping pong
            :param int count: the number of times to repeat the check

        '''
        self.flush()
        for i in range(count):
            current = parsed_email[i]
            current["sendTime"] = dt.timestamp(dt.now())
            assert (self.ping.write(current, block=True))
            # time.sleep(30) # allow 30 seconds for the message to propagate
            msg2 = self.pong.read()
            assert current == msg2