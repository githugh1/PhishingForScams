# PhishingForScams Documentation Guildelines

Sphinx is used to manage the documentation and autogenerate the api from `src`.

:::{note}
PhishingForScams uses `Markdown` docstings documentation with Sphinx `autodoc2` extention and `myst` parser.
For more information, refer to:
https://myst-parser.readthedocs.io/en/latest/index.html
:::

The documentation theme is `ReadTheDocs`. A secondary `requirements.txt` has been added specifically for the packages needed for the documentation of this project.


## Project Tree Structure

The main parts of the project are shown in the structure below. The documentation is predominantly written under `/docs` with the exception of the main `./README.md` file and two other `./tests/README.md` for testing and `./docs/README.md` for documentation. These two were put in those locations as a quick reference and been linked symbolically to `./docs/source` 

```bash
PhishingForScams
├── LICENSE
├── README.md
├── requirements.txt
├── VERSION
├── docs
│   ├── Makefile
│   ├── README.md
│   ├── requirements.txt
│   ├── build
│   ├── make.bat
│   └── source
│       ├── conf.py
│       └── index.rst
├── src
├── tests
│   └── README.md
└── venv

```

## Building the docs with Sphinx

Sphinx configuration is found under `/docs/source/conf.py`

To build the documentation, run the following command under `/docs` directory:
```bash
$ make clean
$ make html
```

## Documentation Examples

Here are some examples regarding the documentation (to bring you upto speed)

### PFS Class
A class has a:
*   short description
*   _blank line_
*   long description
*   _everything else_
::::{admonition} Class Documentation Example
:name: pfs_class_doc_example
:class: tip

:::{code-block} python
:lineno-start: 1

    class kafka_q(queue):
        """This class implements a queue using Kafka.

        It is deriving {class}`src.q.queue` and implements both _read_ and _write_ methods
        inline with Kafka queue implementation.

        #### Attributes:
        - **producer**: ({class}`kafka.KafkaProducer`) -- A handle to kafka producer queue.
                            this is the queue that is used by the _write_ method to produce
                            new item
        - **consumer**: ({class}`kafka.KafkaConsumer`) -- A handle to kafka consumer queue.
                            this is the queue that is used by the _read_ method to consume
                            items

        #### Environment Variables:
        - {envvar}`PFS_KAFKA_SRVR`
                kafka server ip address or DNS identifier (Default: localhost)
        - {envvar}`PFS_KAFKA_PORT`
                kafka server port (Default: 9092)
        - {envvar}`PFS_KAFKA_RQ`
                name of the queue (topic) to read from
        - {envvar}`PFS_KAFKA_WQ`
                name of the queue (topic) to write to
        - {envvar}`PFS_KAFKA_REQUEST_TIMEOUT_MS`
                sets the server request timeouts in milliseconds
                for both the producer and consumer (Default: 3000 ms)
        - {envvar}`PFS_KAFKA_PRODUCER_ID`
                sets the producer id (Default: PFS_PRODUCER)
        - {envvar}`PFS_KAFKA_COMSUMER_ID`
                sets the consumer id (Default: PFS_CONSUMER)
        - {envvar}`PFS_KAFKA_COMSUMER_GROUP_ID`
                sets the consumer group id (Default: PFS_CONSUMER_GROUP)


        #### Raises:
        - {class}`QException`: exception when errors are detected or mandatory
                                environment variables are not set
        """
:::

::::


### PFS Method
::::{admonition} Method Documentation Example
:name: pfs_method_doc_example
:class: tip

:::{code-block} python
:lineno-start: 1

    def test_ping_pong(self, msg: dict, count: int) -> None:
        ''' checks the consistency of {py:class}`kafka_q` messaging

            {py:data}`ping` and {py:data}`pong` topics are reveresed by design.
            This function sends a message to ping using {py:meth}`src.q.kafka_q.kafka_q.write`
            then reads it back from pong using {py:meth}`src.q.kafka_q.kafka_q.read` and
            checks if it is consistent with the original message.

            :param dict msg: a message to send through ping pong
            :param int count: the number of times to repeat the check

        '''
:::

::::

### PFS Data (Variable)

::::{admonition} Data (Variable) Documentation Example
:name: pfs_data_doc_example
:class: tip

:::{code-block} python
:lineno-start: 1

    log_file: str = os.getenv("PFS_LOG_FILE", _log_file)
    ''' a log file can be set using env var {envvar}`PFS_LOG_FILE` in production (Default: not set!).

        if the environment is not production, then by default logs will be writted to *pfs_log_file.log*
    '''
:::

::::
