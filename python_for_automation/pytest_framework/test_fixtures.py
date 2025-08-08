import pytest

 # setup and tear down methods
@pytest.fixture
def setup():
     age = 25
     print(age , "I will execute first")
     yield
     print("I'm tear down")

def test_fix(setup):
     print("I'm going to execute 2nd after the initial setup")