import pytest


@pytest.fixture
def set_up_func():
    print("This is a set up function")

def test_func1(set_up_func):
    print()
    print("This is inside test function")