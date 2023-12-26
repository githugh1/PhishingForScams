
# A Python parsing service to convert raw eml data into actionable data via json

# Uses MailParse 1.0.13 (https://pypi.org/project/mailparse/) (will need to be added to requirements.txt) -> (mailparse==1.0.13)
# Setup: pip install mailparse

import json
from mailparse import EmailDecode

class EmailParser:

    def __init__(self):
        pass

    def parse_email(self, file):
        
        decoded = EmailDecode.open(file)
        return(json.dumps(decoded, indent=4))