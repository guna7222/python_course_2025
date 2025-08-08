# any pytest file should start with test_ or end with _test
import pytest
# use functions pytest standard
# any code should wrap with methods
def test_first_program():  # test method should start with test_
    print("Pytest")

# py.test filename -v -s
# method names execution -k
# -v for more info
# -s logs in output
# py.test -k CreditCard -v -s
# -m for mark

def test_good_evening_greetings():
    msg = "good evening"
    assert msg == "good evening", "greetings error"

@pytest.mark.calculations # custom mark
def test_addition():
    a = b =5
    c = a + b
    assert c == 10

# skipping thi test for now

@pytest.mark.calculations
@pytest.mark.skip
def test_substraction():
    a = b = 5
    c = a - b
    assert c == 5

@pytest.mark.xfail
def test_multiplication():
    a = b = 5
    c = a * b
    assert c == 15