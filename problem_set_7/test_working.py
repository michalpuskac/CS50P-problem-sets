import pytest
from working import convert

def test_convert_valid_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:00 AM") == "22:30 to 08:00"

def test_convert_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_convert_invalid_hours():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 25:00 PM")

def test_convert_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")