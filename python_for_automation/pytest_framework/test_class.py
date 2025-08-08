import pytest

@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('data_driven')
class Testing:

    def test_case1(self):
        print("I'm first test case")

    def test_case2(self):
        print("I'm second test case ")

    # data driven fixtures
    def test_data_driven(self, data_driven):
        print(data_driven[0])

