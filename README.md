# PhishingForScams
Project at the intersection of ML and Cybersecurity. Aiming to create an interface which predicts whether an email is phishing using NLP techniques and redirects users based on the results of the ML model.

For the developer documentation about the Architecture and APIs of **PhishingForScams** refer to the [docs](./docs "Docs") directory. For the testing documentation refer to the [tests](./tests/README.md "Test README") directory.

## Quick Starting Guide

To setup this project, follow these steps:

+ [setup the virtual environement](#setup-the-virtual-environment)
+ [setup Kafka](#setup-kafka)


### Setup the virtual environment

1. `virtualenv -p3 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

### Setup Kafka
-----------
**You need to setup the virtual environment and source it first!**
The script `kafka.bash` is provided to download and launch [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka") for you.

Running `kafka.bash` assumes that you have installed docker. If you havent then it is recommended to install `#0969DA` _Docker Desktop_ per the instructions on [Docker](https://www.docker.com/get-started/ "Docker") website.

#### Download [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka"):
`bash kafka.bash create`

#### Launch [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka"):
`bash kafka.bash up`

#### Terminate [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka"):
`bash kafka.bash down`

## Configuration
TBA

## Running PhishingForScam Service
TBA