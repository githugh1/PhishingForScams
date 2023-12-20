
# A Python parsing service to convert raw email data into actionable data via json
# To Do:
#   - Integrate API
#   - Discuss Byte Parsing
#   - Resolve pytest issue

import json, email

class EmailParser:
    """
    A class for parsing email metadata and content.

    Attributes:
    None

    Methods:
    - parse_email(json_input): Parse the JSON input containing email metadata and return a JSON-formatted result.
    - parse_metadata(metadata): Parse email metadata and return a dictionary with relevant information.
    - parse_field(msg, field): Parse a specific field from the email message.
    - parse_body_attachments(msg): Parse the body and attachments of the email message.

    Example:
    ```
    parser = EmailParser()
    result = parser.parse_email(json.dumps(email_content))
    ```

    """

    def __init__(self):
        """
        Initializes an EmailParser instance.

        Args:
        None

        Returns:
        None
        """

        pass

    def parse_email(self, json_input):
        """
        Parse JSON-formatted email input and return a JSON-formatted result.

        Args:
        - json_input (str): JSON-formatted input containing email metadata.

        Returns:
        - str: JSON-formatted result of the parsed email.

        Example:
        ```
        result = parse_email(json.dumps(email_content))
        ```

        """

        input_data = json.loads(json_input)
        metadata = input_data.get("metadata", "")
        parsed_email = self.parse_metadata(metadata)
        parsed_email["consumer_id"] = input_data.get("consumer_id", "")
        return json.dumps(parsed_email)

    def parse_metadata(self, metadata):
        """
        Parse email metadata and return a dictionary with relevant information.

        Args:
        - metadata (str): String containing email metadata.

        Returns:
        - dict: Dictionary containing parsed email information.

        Example:
        ```
        result = parse_metadata(metadata)
        ```

        """

        msg = email.message_from_string(metadata)
        parsed_email = {
            "consumer_id": "",
            "from": self.parse_field(msg, "From"),
            "to": self.parse_field(msg, "To"),
            "cc": self.parse_field(msg, "Cc"),
            "bcc": self.parse_field(msg, "Bcc"),
            "subject": self.parse_field(msg, "Subject"),
            "date": self.parse_field(msg, "Date"),
            "message_id": self.parse_field(msg, "Message-ID"),
            "received": self.parse_field(msg, "Received"),
            "mime_version": self.parse_field(msg, "MIME-Version"),
            "user_agent": self.parse_field(msg, "User-Agent"),
            "body": {},
            "attachments": []
        }

        parsed_email.update(self.parse_body_attachments(msg))

        return parsed_email

    def parse_field(self, msg, field):
        """
        Parse a specific field from the email message.

        Args:
        - msg (email.Message): Email message object.
        - field (str): Field to be parsed.

        Returns:
        - str or list: Parsed field value.

        Example:
        ```
        result = parse_field(msg, "From")
        ```

        """

        data = msg.get(field, "")
        if (field == "Cc" or field == "Bcc"):
            return [addr.strip() for addr in data.split(",")]
        else:
            return data

    def parse_body_attachments(self, msg):
        """
        Parse the body and attachments of the email message.

        Args:
        - msg (email.Message): Email message object.

        Returns:
        - dict: Dictionary containing parsed body and attachments information.

        Example:
        ```
        result = parse_body_attachments(msg)
        ```

        """

        body_found = False
        attachments = []

        body = {
            "content_type": "",
            "data": ""
        }

        for part in msg.walk():
            content_type = part.get_content_type()

            if content_type == "text/plain" and not body_found:
                body["content_type"] = content_type
                body["data"] = part.get_payload()
                body_found = True
            elif content_type.startswith("application/"):
                attachment = {
                    "content_type": content_type,
                    "filename": part.get_filename(),
                    "data": part.get_payload(decode=True)
                }
                attachments.append(attachment)

        return {"body": body, "attachments": attachments}
