from problem_set_2.plates import is_valid

def test_valid_plate():
    assert is_valid("AB123") == True
    assert is_valid("XY987") == True
    assert is_valid("CD456") == True

def test_invalid_license_plate():
    assert is_valid("123AB") == False  # Doesn't start with a letter
    assert is_valid("ABC1234") == False  # Too long
    assert is_valid("A01234") == False  # Starts with a letter but has an invalid second character
    assert is_valid("AB-123") == False  # Contains punctuation

def test_minimum_length():
    assert is_valid("AB") == True

def test_zero_as_second_character():
    assert is_valid("A0XYZ") == False

def test_alphanumeric_input():
    assert is_valid("ABCD12") == True
    assert is_valid("XYZ567") == True
