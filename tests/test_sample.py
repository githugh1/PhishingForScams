import pytest

# content of test_class.py
class TestSample:
    def test_pass(self):
        x = "this is x"
        assert "h" in x

    def test_fail(self):
        x = "hello"
        assert hasattr(x, "check")