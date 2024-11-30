import pytest
from problem_set_3.fuel import get_fraction, calculate_percentage

def test_get_fraction(monkeypatch):
    # Test valid input
    inputs = iter(["3/4", "2/3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_fraction() == (3, 4)
    assert get_fraction() == (2, 3)
    
    # Test invalid input then valid input
    inputs = iter(["5/0", "a/b", "3/2", "2/5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_fraction() == (2, 5)

def test_calculate_percentage():
    # Test calculation correctness
    assert calculate_percentage(1, 4) == 25
    assert calculate_percentage(1, 2) == 50
    assert calculate_percentage(3, 4) == 75
    assert calculate_percentage(99, 100) == 99
    assert calculate_percentage(100, 100) == 100