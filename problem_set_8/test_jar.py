from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("invalid")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)  # Exceeds capacity

def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(5)  # Not enough cookies