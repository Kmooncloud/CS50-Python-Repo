from plates import is_valid
import pytest
#four or more tests for plates.py

def test_lett_start():
    assert is_valid("12") == False
    assert is_valid("AB") == True

def test_two_six():
    assert is_valid("Longerthan") == False

def test_num_rule0():
    assert is_valid("AB123C") == False

def test_num_rule1():
    assert is_valid("ABC012") == False

def test_no_punct():
    assert is_valid("ABC,12") == False

def tes_default():
    assert is_valid("ABC123") == True