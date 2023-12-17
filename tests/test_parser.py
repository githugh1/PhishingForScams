
# A pytest file designed to validate design of emailparser.py

import json
import pytest
from src.utils.myconstants import CONTENT, ATTACHMENTS, BODY, EXPECTED
from src.emailparser import EmailParser

@pytest.fixture
def email_parser():
    """
    Fixture to create an EmailParser instance.

    Returns:
    - EmailParser: Instance of the EmailParser class.
    """

    return EmailParser()

@pytest.fixture
def parsed_email(email_parser):
    """
    Fixture to parse the email content using the EmailParser.

    Args:
    - email_parser (EmailParser): Fixture providing an instance of the EmailParser class.

    Returns:
    - dict: Parsed email content.
    """

    decoded = email_parser.parse_email(json.dumps(CONTENT))
    return json.loads(decoded)

def test_parse_sender(parsed_email):
    """
    Test parsing of the 'from' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["from"] == "john.doe@example.com"

def test_parse_recipient(parsed_email):
    """
    Test parsing of the 'to' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["to"] == "jane.smith@example.com"

def test_parse_cc(parsed_email):
    """
    Test parsing of the 'cc' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["cc"] == ["boss@example.com", "colleague@example.com"]

def test_parse_bcc(parsed_email):
    """
    Test parsing of the 'bcc' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["bcc"] == ["secret.contact@example.com"]

def test_parse_subject(parsed_email):
    """
    Test parsing of the 'subject' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["subject"] == "Meeting Agenda"

def test_parse_date(parsed_email):
    """
    Test parsing of the 'date' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["date"] == "Tue, 4 Dec 2023 15:30:00 +0000"

def test_parse_message_id(parsed_email):
    """
    Test parsing of the 'message_id' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["message_id"] == "<1234567890@example.com>"

def test_parse_received(parsed_email):
    """
    Test parsing of the 'received' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    expected_received = """from mail.example.com (mail.example.com [192.168.1.1]) 
        by smtp.example.net (Postfix) with ESMTP id ABCD1234 
        for <recipient@example.net>; Tue, 4 Dec 2023 15:30:00 +0000 (UTC)"""

    assert parsed_email["received"] == expected_received

def test_parse_MIME(parsed_email):
    """
    Test parsing of the 'mime_version' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["mime_version"] == "1.0"

def test_parse_user_agent(parsed_email):
    """
    Test parsing of the 'user_agent' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    expected_user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    assert parsed_email["user_agent"] == expected_user_agent

def test_parse_body(parsed_email):
    """
    Test parsing of the email body.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["body"] == BODY

def test_parse_attachments(parsed_email):
    """
    Test parsing of email attachments.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["attachments"] == ATTACHMENTS

def test_parse_consumer_id(parsed_email):
    """
    Test parsing of the 'consumer_id' field.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email["consumer_id"] == "123456789"

def test_parse_email(parsed_email):
    """
    Test the overall parsing of the email.

    Args:
    - parsed_email (dict): Fixture providing the parsed email content.

    Returns:
    None
    """

    assert parsed_email == EXPECTED

# Remnant from Unittest
#if __name__ == '__main__':
#    unittest.main()