from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zerio():
    assert square(0) == 0

def test_str():     # tests that the TypeError is raised when a stirng is input
    with pytest.raises(TypeError):
        square("cat")
