#!/bin/bash

directory="/home/mailservice/mail/new"

for file in "$directory"/*; do

    if [[ -f "$file" ]]; then
        python3 q_mail_p.py --write-to-kafka "$file"

        mv "$file" /home/mailservice/mail/old/
    fi
    
done