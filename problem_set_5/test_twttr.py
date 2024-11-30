import pytest
from problem_set_2.twttr import shorten

def test_shorten_no_vowels():
    assert shorten("Hello") == "Hll"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_with_consonants():
    assert shorten("Python is great") == "Pythn s grt"
