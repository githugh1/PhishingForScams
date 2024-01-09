#!/usr/bin/env python

# A Python parsing service to convert raw eml data into actionable data via json

# Uses MailParse 1.0.13 (https://pypi.org/project/mailparse/)
# Setup: pip install mailparse

# Uses mysql-connector-python 8.2.0 (https://pypi.org/project/mailparse/)
# Setup: pip install mysql-connector-python

# Helpful Guide: https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
# See root README for temporary usage instructions

import json
from mailparse import EmailDecode
import argparse, mysql.connector

CONFIG = {
    'host': 'localhost', # Sub with IP address in future servers
    'user': 'root', # Could change with additional users
    'password': 'your_password',
    'database': 'phishing_for_scams', 
    'port': '3306',
    'raise_on_warnings': True
}

class EmailParser:

    def __init__(self, db_config):
        self.db_config = db_config

    def parse_email(self, file):
        
        decoded = EmailDecode.open(file)
        self.insert_into_table(decoded)
        return json.dumps(decoded, indent=4)
    
    def connect_to_db(self):
        return mysql.connector.connect(**self.db_config)

    def create_table(self):
        connection = self.connect_to_db()
        cursor = connection.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS email_json (
                sender_eml VARCHAR(320) DEFAULT NULL,
                sender_name VARCHAR(1000) DEFAULT NULL,
                recipient_eml VARCHAR(320) DEFAULT NULL,
                recipient_name VARCHAR(1000) DEFAULT NULL,
                eml_subject TEXT DEFAULT NULL,
                message_id TEXT DEFAULT NULL,
                mime_version VARCHAR(10) DEFAULT NULL,
                send_date VARCHAR(100) DEFAULT NULL,
                eml_timestamp INT DEFAULT NULL,
                body LONGTEXT DEFAULT NULL,
                attachments LONGTEXT DEFAULT NULL,
                headers LONGTEXT DEFAULT NULL,
                full_eml LONGTEXT DEFAULT NULL
            )
        """
        cursor.execute(create_table_query)
        connection.commit()

        cursor.close()
        connection.close()

    def insert_into_table(self, email_data):
            
        connection = self.connect_to_db()
        cursor = connection.cursor()

        sender_eml = email_data.get("from", {}).get("email", None)
        sender_name = email_data.get("from", {}).get("name", None)
        recipient_eml = email_data.get("headers", {}).get("Delivered-To", {}).get("email", None)
        recipient_name = email_data.get("headers", {}).get("Delivered-To", {}).get("name", None)
        eml_subject = email_data.get("subject", None)
        message_id = email_data.get("message-id", None)
        mime_version = email_data.get("headers", {}).get("Mime-Version", None)
        send_date = email_data.get("date", None)
        eml_timestamp = email_data.get("timestamp", None)
        body = email_data.get("text", None)
        attachments = email_data.get("attachments", None)
        headers = email_data.get("headers", None)
        full_eml = json.dumps(email_data, indent=4)

        query = """INSERT INTO email_json 
                        (sender_eml, sender_name, recipient_eml, recipient_name, eml_subject, 
                        message_id, mime_version, send_date, eml_timestamp, body, attachments, 
                        headers, full_eml) 
                        VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.execute(query, (
            sender_eml, sender_name, recipient_eml, recipient_name, eml_subject,
            message_id, mime_version, send_date, eml_timestamp, body,
            json.dumps(attachments) if attachments is not None else None,
            json.dumps(headers) if headers is not None else None,
            full_eml
        ))

        connection.commit()

        cursor.close()
        connection.close()

# Parse and Print using: python path/to/parser.py path/to/file.eml

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    args = parser.parse_args()

    email_parser = EmailParser(CONFIG)
    parsed_email = email_parser.parse_email(args.file)

    # Print to Terminal - Optional
    print(parsed_email)