import sys
import os
import smtplib
from email import message_from_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender, recipient, subject, body, attachments, smtp_host, smtp_port, smtp_username, smtp_password):
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for attachment in attachments:
        with open(attachment, "rb") as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(attachment))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
        msg.attach(part)

    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_email.py <eml_file>")
        sys.exit(1)

    eml_file_path = sys.argv[1]

    with open(eml_file_path, 'r') as eml_file:
        eml_content = eml_file.read()

    eml_message = message_from_string(eml_content)

    sender = eml_message['From']
    recipient = 'lachlanbdoak@gmail.com' #eml_message['To']
    subject = eml_message['Subject']
    body = ""

    for part in eml_message.walk():
        content_type = part.get_content_type()
        filename = part.get_filename()
        if content_type == "text/plain" and not filename:
            body += part.get_payload(decode=True).decode()
        elif filename:
            attachment_data = part.get_payload(decode=True)
            with open(filename, 'wb') as f:
                f.write(attachment_data)

    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'phishingforscams'
    smtp_password = 'wouy bwop eyui ekys'

    attachments = []

    send_email(sender, recipient, subject, body, attachments, smtp_host, smtp_port, smtp_username, smtp_password)