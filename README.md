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

### Setup MySQL
-----------
**You need to download MySQL First!**
The MySQL Community Edition can be found [here](https://dev.mysql.com/downloads/installer/). (Script in progress)

Follow the setup instructions as outlined in [this video](https://www.youtube.com/watch?v=wgRwITQHszU).

Once you have opened a localhost server in MySQL, select 'new Query', then navigate to this project directory and select src\db\phishing_for_scams_db.sql
At the top of the database, select execute (lightning symbol) and then refresh the Schema via the button in the top right of the window to create the database. --> (will be altered in future)

#### Running The Parser
To run email_parser in terminal and parse an email to the database, you must alter the CONFIG of email_parser first. To run on localhost, you must only input your selected password. Everything else has been provided.

Before running, ensure you have installed all requirements via the text file. To run the parser, simply navigate to the root directory and execute `python src/parser/email_parser.py path/to/file.eml`. Refresh your schema window on mySQL and the table will be updated with the new data. (Will be improved with scripting in future)

## Configuration
TBA

## Running PhishingForScam Service
TBA