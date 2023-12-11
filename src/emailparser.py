
import json, email

class EmailParser:

    def __init__(self):
        pass

    def parse_email(self, json_input):
        input = json.loads(json_input)
        metadata = input.get("metadata", "")
        parsed_email = self.parse_metadata(metadata)
        parsed_email["consumer_id"] = input.get("consumer_id", "")
        return json.dumps(parsed_email)

    def parse_metadata(self, metadata):
        msg = email.message_from_string(metadata)
        parsed_email = {
            "consumer_id": "",
            "from": self.parse_sender(self, msg, "From"),
            "to": self.parse_recipient(self, msg, "To"),
            "cc": self.parse_cc(self, msg, "Cc"),
            "bcc": self.parse_bcc(self, msg, "Bcc"),
            "subject": self.parse_subject(self, msg, "Subject"),
            "date": self.parse_date(self, msg, "Date"),
            "message_id": self.parse_message_id(self, msg, "Message-ID"),
            "received": self.parse_received(self, msg, "Received"),
            "mime_version": self.parse_mime_version(self, msg, "MIME-Version"),
            "user_agent": self.parse_user_agent(self, msg, "User-Agent"),
            "body": {},
            "attachments": []
        }

        parsed_email.update(self.parse_body_attachments(msg))

        return parsed_email

    def parse_body_attachments(self, msg):
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
    
    def parse_sender(self, msg):
        return msg.get("From", "")

    def parse_recipient(self, msg):
        return msg.get("To", "")

    def parse_cc(self, msg):
        cc = msg.get("Cc", "")
        return [addr.strip() for addr in cc.split(",")]

    def parse_bcc(self, msg):
        bcc = msg.get("Bcc", "")
        return [addr.strip() for addr in bcc.split(",")]

    def parse_subject(self, msg):
        return msg.get("Subject", "")

    def parse_date(self, msg):
        return msg.get("Date", "")

    def parse_message_id(self, msg):
        return msg.get("Message-ID", "")

    def parse_received(self, msg):
        return msg.get("Received", "")

    def parse_mime_version(self, msg):
        return msg.get("MIME-Version", "")

    def parse_user_agent(self, msg):
        return msg.get("User-Agent", "")
    
    def parse_field(self, msg, field):
        data = msg.get(field, "")
        if (field == "Cc" | field == "Bcc"):
            return [addr.strip() for addr in data.split(",")]
        else:
            return data
