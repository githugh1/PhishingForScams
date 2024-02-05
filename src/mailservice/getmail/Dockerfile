FROM python:slim

WORKDIR /home/mailservice

COPY requirements.txt .

RUN useradd -u 1000 mailuser && \
    mkdir -p ./mail/cur ./mail/tmp ./mail/new && \
    chown -R mailuser:mailuser ./mail/ && \
    chmod -R 700 ./mail/ && \
    pip3 install -r requirements.txt && \
    chown -R mailuser:mailuser /home/mailservice/mail

USER mailuser

# Sleep 'n' seconds -> periodically pull emails
CMD ["bash", "-c", "while true; do getmail --getmaildir getmail/config; sleep 300; done"]