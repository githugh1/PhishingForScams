Running Pytest
==============
All the testing need to be put under the [tests](./tests/ "tests") directory in the main project. The pytest file needs to start with the name `test_`\<file_name\> and so all the test functions need to be named as `test_`\<function_name\>! See [pytest](https://docs.pytest.org/en/stable/getting-started.html "Pytest") documentation for details.

To run pytest, from the main project directory run one of the following:
- To run all the test, run `pytest`
- To see a verbose output, run `pytest -v` or `pytest -vvv`
- To run the tests for a sepcific test file, run `pytest tests/test_sample.py`
- To run the tests for one **class** only, run `pytest tests/test_sample.py::TestSample`
- To run the test for one **test function** only, run `pytest tests/test_sample.py::TestSample::test_pass`
