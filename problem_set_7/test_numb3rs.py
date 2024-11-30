from numb3rs import validate

def test_valid_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_invalid_addresses():
    assert validate("275.3.6.28") == False  # Invalid part 275
    assert validate("192.168.1.256") == False  # Invalid part 256
    assert validate("192.168.1") == False  # Missing part
    assert validate("192.168.1.1.1") == False  # Extra part
    assert validate("192.168.a.1") == False  # Non-numeric part
    assert validate("192.168.-1.1") == False  # Negative number
    assert validate("192.168.01.1") == False  # Leading zero

def test_edge_cases():
    assert validate("1.2.3.4") == True  # Minimum valid numbers
    assert validate("001.002.003.004") == False  # Leading zeros