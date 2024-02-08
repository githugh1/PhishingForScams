FROM python:3.11-slim

WORKDIR /home/mailservice

COPY mailservice/requirements.txt .
COPY mailservice/q_mail_p.py .
COPY mailservice/q_mail.sh .
COPY parser/email_parser.py .

RUN mkdir src

COPY q/* src/q/
COPY utils/* src/utils/

RUN useradd -u 1000 mailuser && \
    mkdir -p ./mail/cur ./mail/tmp ./mail/new ./mail/old && \
    chown -R mailuser:mailuser ./mail/ && \
    chmod -R 700 ./mail/ && \
    pip3 install --no-cache-dir -r requirements.txt && \
    chown -R mailuser:mailuser /home/mailservice

USER mailuser



# Sleep 'n' seconds -> periodically pull emails
CMD ["bash", "-c", "while true; do getmail --getmaildir getmail/config; bash q_mail.sh; sleep 300; done"]