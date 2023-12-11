
METADATA = """
From: john.doe@example.com
To: jane.smith@example.com
Cc: boss@example.com, colleague@example.com
Bcc: secret.contact@example.com
Subject: Meeting Agenda
Date: Tue, 4 Dec 2023 15:30:00 +0000
Message-ID: <1234567890@example.com>
Received: from mail.example.com (mail.example.com [192.168.1.1])
    by smtp.example.net (Postfix) with ESMTP id ABCD1234
    for <recipient@example.net>; Tue, 4 Dec 2023 15:30:00 +0000 (UTC)
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="boundary123"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36

--boundary123
Content-Type: text/plain; charset="utf-8"

Hello Jane,

Please find attached the agenda for our upcoming meeting.

Best regards,
John

--boundary123
Content-Type: application/pdf
Content-Disposition: attachment; filename="meeting_agenda.pdf"

[Binary data of the PDF file]

--boundary123--
Content-Type: image/jpeg
Content-Disposition: attachment; filename="photo.jpg"

[Binary data of the JPEG file]

--boundary123--
"""

CONTENT = {
    "consumer_id": "1234567890",
    """metadata""": METADATA
}

BODY = {
    "content_type": "text/plain",
    "data": """Hello Jane,

            Please find attached the agenda for our upcoming meeting.

            Best regards,
            John"""
}

ATTACHMENTS = [
    {
    "content_type": "application/pdf",
    "filename": "meeting_agenda.pdf",
    "data": "[Binary data of the PDF file]"
    },
    {
    "content_type": "image/jpeg",
    "filename": "photo.jpg",
    "data": "[Binary data of the JPEG file]"
    },
]

EXPECTED = {
    "consumer_id": "123456789",
    "from": "john.doe@example.com",
    "to": "jane.smith@example.com",
    "cc": ["boss@example.com", "colleague@example.com"],
    "bcc": ["secret.contact@example.com"],
    "subject": "Meeting Agenda",
    "date": "Tue, 4 Dec 2023 15:30:00 +0000",
    "message_id": "<1234567890@example.com>",
    "received": """from mail.example.com (mail.example.com [192.168.1.1]) 
            by smtp.example.net (Postfix) with ESMTP id ABCD1234 
            for <recipient@example.net>; Tue, 4 Dec 2023 15:30:00 +0000 (UTC)""",
    "mime_version": "1.0",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "body": {
        "content_type": "text/plain",
        "data": """Hello Jane,

            Please find attached the agenda for our upcoming meeting.

            Best regards,
            John"""
    },
    "attachments": [
        {
            "content_type": "application/pdf",
            "filename": "meeting_agenda.pdf",
            "data": "[Binary data of the PDF file]"
        },
        {
            "content_type": "image/jpeg",
            "filename": "photo.jpg",
            "data": "[Binary data of the JPEG file]"
        },
    ]
}