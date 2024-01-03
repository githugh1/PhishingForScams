
import json, pytest
from src.parser.email_parser import EmailParser
from .utils.expected_outputs import EXPECTED_EML_3

# source venv/Scripts/activate

class TestParser:

    # Fixtures included for a consistent test base

    @pytest.fixture
    def email_parser(self):
        return EmailParser()
    
    @pytest.fixture
    def parsed_email(self, email_parser):
        decoded = email_parser.parse_email('tests/data/example3.eml')
        return json.loads(decoded)

    # Standard testing methods for common fields

    def test_parse_from(self, parsed_email):
        print(parsed_email)
        assert parsed_email["from"] ==  EXPECTED_EML_3["from"], "From Does Not Match"

    def test_parse_to(self, parsed_email):
        with pytest.raises(KeyError):
            assert parsed_email["to"] == EXPECTED_EML_3["to"], "To Does Not Match"

    def test_parse_subject(self, parsed_email):
        assert parsed_email["subject"] == EXPECTED_EML_3["subject"], "Subjects Do Not Match"

    def test_parse_date(self, parsed_email):
        assert parsed_email["date"] == EXPECTED_EML_3["date"], "Dates Do Not Match"

    def test_parse_message_id(self, parsed_email):
        assert parsed_email["message-id"] == EXPECTED_EML_3["message-id"], "Message-Ids Do Not Match"

    def test_parse_received(self, parsed_email):
        assert parsed_email["headers"]["Received"] == EXPECTED_EML_3["headers"]["Received"], "Headers Do Not Match"

    def test_parse_MIME(self, parsed_email):
        assert parsed_email["headers"]["Mime-Version"] == EXPECTED_EML_3["headers"]["Mime-Version"], "MIME Does Not Match"

    def test_parse_text(self, parsed_email):
        assert parsed_email["text"] == EXPECTED_EML_3["text"], "Texts Do Not Match"

    def test_parse_attachments(self, parsed_email):
        with pytest.raises(KeyError):
            assert parsed_email["attachments"] == EXPECTED_EML_3["attachments"], "Attachments Do Not Match"

    # For testing any fields unique to the example

    def test_parse_email(self, parsed_email):
        for key, value in parsed_email.items():
            assert key in EXPECTED_EML_3
            assert EXPECTED_EML_3[key] == value, "Outputs Do Not Match"