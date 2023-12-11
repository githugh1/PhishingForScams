
import unittest, json
from utils.myconstants import CONTENT, ATTACHMENTS, BODY, EXPECTED
from src.emailparser import EmailParser

class TestParser(unittest.TestCase):
    
    def setUp(self):
        self.parser = EmailParser()
        decode = self.parser.parse_email(json.dumps(CONTENT))
        self.result = json.loads(decode)

    def tearDown(self):
        pass

    def test_parse_sender(self):
        self.assertEqual(self.result["from"], "john.doe@example.com")

    def test_parse_recipient(self):
        self.assertEqual(self.result["to"], "jane.smith@example.com")

    def test_parse_cc(self):
        self.assertEqual(self.result["cc"], ["boss@example.com", "colleague@example.com"])

    def test_parse_bcc(self):
        self.assertEqual(self.result["bcc"], ["secret.contact@example.com"])

    def test_parse_subject(self):
        self.assertEqual(self.result["subject"], "Meeting Agenda")

    def test_parse_date(self):
        self.assertEqual(self.result["date"], "Tue, 4 Dec 2023 15:30:00 +0000")

    def test_parse_message_id(self):
        self.assertEqual(self.result["message_id"], "<1234567890@example.com>")
    
    def test_parse_received(self):
        self.assertEqual(self.result["received"], """from mail.example.com (mail.example.com [192.168.1.1]) 
            by smtp.example.net (Postfix) with ESMTP id ABCD1234 
            for <recipient@example.net>; Tue, 4 Dec 2023 15:30:00 +0000 (UTC)""")

    def test_parse_MIME(self):
        self.assertEqual(self.result["mime_version"], "1.0")

    def test_parse_user_agent(self):
        self.assertEqual(self.result["user_agent"], "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    def test_parse_body(self):
        self.assertEqual(self.result["body"], BODY)

    def test_parse_attachments(self):
        self.assertEqual(self.result["attachments"], ATTACHMENTS)

    def test_parse_consumer_id(self):
        self.assertEqual(self.result["consumer_id"], "123456789")
    
    def test_parse_email(self):
        self.assertEqual(self.result, EXPECTED)

if __name__ == '__main__':
    unittest.main()