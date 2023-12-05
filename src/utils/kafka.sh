#!/bin/bash

if [ 'x'$1 == 'create' ];
then
    mkdir kafka; 
    cd kafka;
    git clone https://github.com/sulphurcrested/kafka.git;
elif [ 'x'$1 == 'up' ];
then
    docker-compose -f docker-compose.yml up --build --no-cache --detach kafka;
elif [ 'x'$1 == 'down' ];
then
    docker-compose -f docker-compose.yml down kafka;
else
    echo "USAGE: kafka.sh ['create' | 'up' | 'down' ]";
fi
