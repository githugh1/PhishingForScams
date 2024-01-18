#!/usr/bin/env python

# By Lachlan Doak (09-01-2024)
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
    'password': 'Benjamin04',
    'database': 'pfs_stats', 
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
            CREATE TABLE IF NOT EXISTS main (
                id TEXT NOT NULL,
                item_source TEXT DEFAULT NULL,
                time_sent datetime DEFAULT NULL,
                item_key TEXT DEFAULT NULL,
                item_val LONGTEXT NOT NULL
            )
        """
        cursor.execute(create_table_query)
        connection.commit()

        cursor.close()
        connection.close()

    def insert_into_table(self, email_data):
            
        connection = self.connect_to_db()
        cursor = connection.cursor()

        id = email_data.get("message-id", None)
        item_source = "parser"
        item_key = "full_eml"
        item_val = json.dumps(email_data, indent=4)

        query = """INSERT INTO main 
                        (id, item_source, time_sent, item_key, item_val) 
                        VALUES 
                        (%s, %s, now(), %s, %s)"""

        cursor.execute(query, (
            id, item_source, item_key, item_val
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
    # print(parsed_email)