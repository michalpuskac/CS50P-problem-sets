import pytest
from problem_set_1.bank import process

def test_for_0():
    assert process("hello") == 0
    assert process("HELLO") == 0
    assert process("HeLLo") == 0
    
def test_for_20():
    assert process ("hi") == 20
    assert process ("How are you") == 20
    assert process ("heLp") == 20
    
def test_for_100():
    assert process ("Good morning") == 100
    assert process ("50hi") == 100
    
def test_for_empty():
    assert process ("") == 100