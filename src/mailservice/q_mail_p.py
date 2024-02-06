from src.q.kafka_q import kafka_q
import os
import argparse
from src.utils.pfs_logging import log

parser = argparse.ArgumentParser(description='Process EML files and send file paths to kafka')
parser.add_argument('--write-to-kafka', type=str, help='File path to be sent to Kafka')

args = parser.parse_args()

os.environ["PFS_KAFKA_SRVR"] = 'kafka'
os.environ["PFS_KAFKA_PORT"] = '19092'
os.environ["PFS_KAFKA_WQ"] = 'TEST_NEW_EMAILS_Q'
os.environ["PFS_KAFKA_RQ"] = 'NO_READ_Q'

ping: kafka_q = kafka_q()

log.debug(f"ping topics:{ping.consumer.topics()}")

ping.write(args.write_to_kafka, block=True)
