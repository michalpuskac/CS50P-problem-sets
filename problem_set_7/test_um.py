from um import count
import pytest

def test_single_um():
    assert count("hello, um, world") == 1

def test_no_um():
    assert count("yummy food") == 0
    assert count("umbrella") == 0

def test_multiple_ums():
    assert count("Um, um, um...") == 3

def test_um_in_sentence():
    assert count("Um, well, um, I don't know.") == 2
    assert count("Um? I don't think so.") == 1

def test_case_insensitivity():
    assert count("UM, Um, um") == 3
    assert count("UM um") == 2