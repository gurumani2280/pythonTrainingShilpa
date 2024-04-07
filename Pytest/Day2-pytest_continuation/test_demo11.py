import pytest


@pytest.fixture
def set_up_func2():
    print("This is a set up function")
    yield
    print("This will run after the test method is completed")


def test_func2(set_up_func2):
    print()
    print("This is inside test function")
