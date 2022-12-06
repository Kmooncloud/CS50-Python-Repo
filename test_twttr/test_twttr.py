# pset 5 Testing my Twitter
# implement and test updated version of twitter program that removes vowels from a string

import pytest
from twttr import shorten

def test_default():
    assert shorten("") == ""

def test_vowels():
    assert shorten("aeiou") == ""

def test_vowels_upper():
    assert shorten("AEIOU") == ""

def test_prints_upper():
    assert shorten("PrINts UPPeR") == "PrNts PPR"

def test_omit_punct():
    assert shorten("test!?,") == "tst!?,"

def test_omit_num():
    assert shorten("test12") == "tst12"