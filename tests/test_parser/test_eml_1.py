
import json, pytest
from ...src.parser.email_parser import EmailParser
from .utils.expected_outputs import EXPECTED_EML_1

# source venv/Scripts/activate

class TestParser:

    # Fixtures included for a consistent test base

    @pytest.fixture
    def email_parser(self):
        return EmailParser()
    
    @pytest.fixture
    def parsed_email(self, email_parser):
        decoded = email_parser.parse_email('data/example1.eml')
        return json.loads(decoded)

    # Standard testing methods for common fields

    def test_parse_from(self, parsed_email):
        assert parsed_email["from"] ==  EXPECTED_EML_1["from"]

    def test_parse_to(self, parsed_email):
        assert parsed_email["to"] == EXPECTED_EML_1["to"]

    def test_parse_subject(self, parsed_email):
        assert parsed_email["subject"] == EXPECTED_EML_1["subject"]

    def test_parse_date(self, parsed_email):
        assert parsed_email["date"] == EXPECTED_EML_1["date"]

    def test_parse_message_id(self, parsed_email):
        assert parsed_email["message-id"] == EXPECTED_EML_1["message-id"]

    def test_parse_received(self, parsed_email):
        assert parsed_email["headers"]["Received"] == EXPECTED_EML_1["headers"]["Received"]

    def test_parse_MIME(self, parsed_email):
        assert parsed_email["headers"]["Mime-Version"] == EXPECTED_EML_1["headers"]["Mime-Version"]

    def test_parse_text(self, parsed_email):
        assert parsed_email["text"] == EXPECTED_EML_1["text"]

    def test_parse_attachments(self, parsed_email):
        with pytest.raises(KeyError):
            assert parsed_email["attachments"] == EXPECTED_EML_1["attachments"]

    # For testing any fields unique to the example

    def test_parse_email(self, parsed_email):
        for key, value in parsed_email.items():
            assert key in EXPECTED_EML_1
            assert EXPECTED_EML_1[key] == value