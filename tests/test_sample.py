import pytest

# content of test_class.py
# see https://docs.pytest.org/en/7.3.x/how-to/ for more info

class TestSample:
    def test_positiveTestcase(self):
        x = "this is x"
        assert "h" in x

    def test_negativeTestcase(self):
        x = "hello"
        assert not hasattr(x, "check")
    
    @pytest.mark.xfail
    def test_expectedFailure(self):
        x = "hello"
        assert hasattr(x, "check")
    
    @pytest.mark.xfail
    def test_unexpectedPadd(self):
        x = "this is x"
        assert "h" in x
    
