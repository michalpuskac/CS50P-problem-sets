from seasons import calculate_minutes_lived, convert_to_words
from datetime import date

def test_calculate_minutes_lived():
    birth_date = date(2000, 1, 1)
    today = date(2024, 1, 1)
    expected_minutes = (today - birth_date).days * 24 * 60
    assert calculate_minutes_lived(birth_date, today) == expected_minutes

def test_convert_to_words():
    assert convert_to_words(525600) == "five hundred twenty-five thousand six hundred"
    assert convert_to_words(0) == "zero"
    assert convert_to_words(1) == "one"