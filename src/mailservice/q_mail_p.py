from src.q.kafka_q import kafka_q
import os
import argparse
from src.utils.pfs_logging import log
import json
import time
from datetime import datetime as dt

parser = argparse.ArgumentParser(description='Process EML files and send file paths to kafka')
parser.add_argument('--write-to-kafka', type=str, help='File path to be sent to Kafka')

args = parser.parse_args()

# Dynamic topics somewhat work -> still failing?

_new_topic = dt.timestamp(dt.now())
_topics = [f'Q1-{_new_topic}', f'Q2-{_new_topic}']

os.environ["PFS_KAFKA_SRVR"] = 'kafka'
os.environ["PFS_KAFKA_PORT"] = '19092'
os.environ["PFS_KAFKA_RQ"] = _topics[0]
os.environ["PFS_KAFKA_WQ"] = _topics[1]
ping: kafka_q = kafka_q()


os.environ["PFS_KAFKA_RQ"] = _topics[1]
os.environ["PFS_KAFKA_WQ"] = _topics[0]
pong: kafka_q = kafka_q()

if __name__ == "__main__":
    try:
        log.debug(f"ping topics:{ping.consumer.topics()}")
        msg1 = ping.write({"filepath": args.write_to_kafka}, block=True)
        print(args.write_to_kafka)
        time.sleep(10)

        msg2 = pong.read()
        print(msg1)
        print(msg2)

        

    except Exception as e:
        print(f"Error occurred: {e}")
