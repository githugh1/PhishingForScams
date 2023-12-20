# PhishingForScams Documentation Guildelines

Sphinx is used to manage the documentation and autogenerate the api from `src`.

:::{note}
PhishingForScams uses `Markdown` docstings documentation with Sphinx `napolean` extention and [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

The documentation is produced using `ReadTheDocs` theme
:::



## Project Tree Structure

The main parts of the project are shown in the structure below. The documentation is predominantly written under `/docs` with the exception of the main `./README.md` file and two other `./tests/README.md` for testing and `./docs/README.md` for documentation. These two were put in those locations as a quick reference and been linked symbolically to `./docs/source` 

```bash
PhishingForScams
├── LICENSE
├── README.md
├── VERSION
├── docs
│   ├── Makefile
│   ├── README.md
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

To build the configuration, run the following command under `/docs` directory:
```bash
$ make clean
$ make html
```