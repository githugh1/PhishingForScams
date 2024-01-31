#!/bin/bash

kafka=kafka

is_linux() {
  [[ "$(uname -s)" == "Linux" ]]
}

if [ 'x'$1 == 'xcreate' ];
then
    if [[ -z `ls -1 | grep '^'$kafka'$'` ]];
    then
        git clone https://github.com/sulphurcrested/kafka.git;
    else
        echo $kafka" directory already exists ... updating content";
        `cd $kafka; git pull; cd ..`;
    fi
elif [ 'x'$1 == 'xup' ]; then
    if is_linux; then
        sudo docker compose -f $kafka/docker-compose.yml up --build --detach kafka
        sleep 1
        sudo docker compose -f $kafka/docker-compose.yml up --build --detach db
        sleep 5
        sudo docker compose -f $kafka/docker-compose.yml up --build --detach flask
        sleep 5
        sudo docker compose -f $kafka/docker-compose.yml up --build --detach node
    else
        docker compose -f $kafka/docker-compose.yml up --build --detach kafka
        sleep 1
        docker compose -f $kafka/docker-compose.yml up --build --detach db
        sleep 5
        docker compose -f $kafka/docker-compose.yml up --build --detach flask
        sleep 5
        docker compose -f $kafka/docker-compose.yml up --build --detach node
    fi
elif [ 'x'$1 == 'xdown' ]; then
    if is_linux; then
        sudo docker compose -f $kafka/docker-compose.yml down node
        sleep 1
        sudo docker compose -f $kafka/docker-compose.yml down flask
        sleep 1
        sudo docker compose -f $kafka/docker-compose.yml down db
        sleep 1
        sudo docker compose -f $kafka/docker-compose.yml down kafka
    else
        docker compose -f $kafka/docker-compose.yml down node
        sleep 1
        docker compose -f $kafka/docker-compose.yml down flask
        sleep 1
        docker compose -f $kafka/docker-compose.yml down db
        sleep 1
        docker compose -f $kafka/docker-compose.yml down kafka
    fi
else
    echo "USAGE: kafka.sh ['create' | 'up' | 'down' ]";
fi
