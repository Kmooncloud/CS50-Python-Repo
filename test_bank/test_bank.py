# pset5 Back to the Bank
# tests bank.py 

import pytest
from bank import value

# three or more function checks
def test_hello():
    assert value("hello") == 0

def test_Hello():
    assert value("Hello") == 0

def test_h():
    assert value("hey there") == 20

def test_not_h():
    assert value("What's up?") == 100