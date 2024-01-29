# PhishingForScams Developer Guide
For contributing to this project, follow these steps to get started:
1. Review the architecture
2. [Setup your environment](#setting-up-your-environment "Setting up your environment")
3. Review the dev documentation
4. Review the [Test](./tester.md) documentation
5. Review the documentation guidelines

## Setting up your environment

To setup this project, follow these steps:

+ [setup the virtual environement](#setup-the-virtual-environment)
+ [setup Kafka](#setup-kafka)

### Setup the virtual environment

1. `virtualenv -p3 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

### Setup Kafka

**You need to setup the virtual environment and source it first!**
The script `kafka.bash` is provided to download and launch [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka") for you.

Running `kafka.bash` assumes that you have installed docker. If you havent then it is recommended to install _Docker Desktop_ per the instructions on [Docker](https://www.docker.com/get-started/ "Docker") website.

#### Download [kafka](<https://github.com/sulphurcrested/kafka> "sulphurcrested/kafka"):
`bash kafka.bash create`

#### Launch [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka"):
`bash kafka.bash up`

#### Terminate [kafka](https://github.com/sulphurcrested/kafka "sulphurcrested/kafka"):
`bash kafka.bash down`

## Developer API Docuementaion

### API Reference
Refer to the {{ LATEST_API_REF }} section.

### Indices and tables

* {ref}`genindex`
* {ref}`modindex`

<!-- >```{toctree}
:maxdepth: 3

apidocs/index
``` -->




