# To be expanded via some customisable config set by admin

import subprocess
from src.q.kafka_q import kafka_q
import os
from src.utils.pfs_logging import log

os.environ["PFS_KAFKA_SRVR"] = 'kafka'
os.environ["PFS_KAFKA_PORT"] = '19092'
os.environ["PFS_KAFKA_RQ"] = 'SCANNED_EMAILS_Q'
os.environ["PFS_KAFKA_WQ"] = 'POLICED_EMAILS_Q'

ping: kafka_q = kafka_q()

def policy_checker(safety_status, eml_file_path):
    msg = ping.read()
    
    if safety_status in [False, "SCAM"]:
        print("Email is deemed unsafe. EML will not be sent.")
    elif safety_status in [True, "SAFE"]:
        print("Email is deemed safe. Queuing email to be sent back to inbox.")
        
    else:
        print("Invalid safety status. Unable to determine policy.")