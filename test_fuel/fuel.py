from fuel import convert
from fuel import gauge
import pytest
# two or more functions to teat both gauge() and convert()

def test_convert():
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

# correct test, but Check50 doesn't recognize it
def test_convert_ve():
    with pytest.raises(ValueError):
        convert("a/b")

def test_convert_zde():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")