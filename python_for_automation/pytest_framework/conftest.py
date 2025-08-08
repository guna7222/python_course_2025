import pytest

@pytest.fixture(scope="class")
def setup():
    print("I'm going to execute first")
    yield
    print("I'm going to close the resources")

@pytest.fixture()
def data_driven():
    print("data driven example")
    return ["guna", "sekhar"]

@pytest.fixture(params=["Chrome", "Firefox"])
def cross_browser(request):
    return request.param     