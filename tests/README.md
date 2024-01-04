# PhishingForScams Tester Guide
PhishingForScams uses Pytest for testing.

## Starting with Pytest
All the testing need to be put under the `/tests/` directory in the main project. The pytest file needs to start with the name `test_<file_name>` and so all the test functions need to be named as `test_<function_name>`! See [pytest](https://docs.pytest.org/en/stable/getting-started.html "Pytest") documentation for details.

## Running Pytest
To run pytest, from the main project directory run one of the following:
- To run all the test, run:
    `pytest`
- To see a verbose output, run:
    `pytest -v` or `pytest -vvv`
- To run the tests for a sepcific test file, run:
    `pytest tests/test_sample.py`
- To run the tests for one **class** only, run:
    `pytest tests/test_sample.py::TestSample`
- To run the test for one **test function** only, run:
    `pytest tests/test_sample.py::TestSample::test_pass`

## Examples

From the main project directory, run `pytest -v`

::::{admonition} ** Example 1: ** Running all test cases
:class: tip

:::{code-block}
:linenos: True
:caption: pytest -v
:emphasize-lines: 4

$ pytest -v
===================== test session starts ================================
platform darwin -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/tester/PhishingForScams
configfile: pyproject.toml
testpaths: tests
collected 48 items

tests/test_kafka_q.py ................................              [ 66%]
tests/test_parser.py FFFFFFFFFFFFFF                                 [ 95%]
tests/test_sample.py .F                                             [100%]

===================== FAILURES ===========================================

:::
::::

You can specify a particular test case to run by adding the testcase path.
In the following example we specify to run the test case {py:meth}`test_ping_pong` which is
located in class {py:class}`TestKQ` under the path `tests/test_kafka_q.py`

::::{admonition} ** Example 2: ** Running a specific test case
:class: tip

::: {code-block}
:linenos: True
:caption: pytest -vvv tests/test_kafka_q.py::TestKQ::test_ping_pong
:emphasize-lines: 6

(venv) $ pytest -vvv tests/test_kafka_q.py::TestKQ::test_ping_pong
===================== test session starts ================================
platform darwin -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- /Users/tes
ter/PhishingForScams/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/tester/PhishingForScams
configfile: pyproject.toml
collected 15 items

tests/test_kafka_q.py::TestKQ::test_ping_pong[1-msg0] PASSED        [  6%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[1-msg1] PASSED        [ 13%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[1-msg2] PASSED        [ 20%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[1-msg3] PASSED        [ 26%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[1-msg4] PASSED        [ 33%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[5-msg0] PASSED        [ 40%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[5-msg1] PASSED        [ 46%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[5-msg2] PASSED        [ 53%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[5-msg3] PASSED        [ 60%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[5-msg4] PASSED        [ 66%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[10-msg0] PASSED       [ 73%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[10-msg1] PASSED       [ 80%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[10-msg2] PASSED       [ 86%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[10-msg3] PASSED       [ 93%]
tests/test_kafka_q.py::TestKQ::test_ping_pong[10-msg4] PASSED       [100%]

===================== 15 passed in 85.01s (0:01:25) ======================
(venv) $

:::
::::