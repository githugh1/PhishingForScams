#!/bin/bash

kafka=kafka
if [ 'x'$1 == 'xcreate' ];
then
    if [[ -z `ls -1 | grep '^'$kafka'$'` ]];
    then
        git clone https://github.com/sulphurcrested/kafka.git;
    else
        echo $kafka" directory already exists ... updating content";
        `cd $kafka; git pull; cd ..`;
    fi
elif [ 'x'$1 == 'xup' ];
then
    `docker compose -f $kafka/docker-compose.yml up --build --detach  kafka`;
elif [ 'x'$1 == 'xdown' ];
then
    `docker compose -f $kafka/docker-compose.yml down kafka`;
else
    echo "USAGE: kafka.sh ['create' | 'up' | 'down' ]";
fi
