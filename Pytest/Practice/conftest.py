import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")
    print()


@pytest.fixture()
def dataLoad():
    print("Data to be loaded")
    return ["Shilpa", "Sadheesh", "123.com"]


@pytest.fixture(params=[("chrome", "Shilpa"), ("firefox", "pop"), ("Edge", "lop")])
def crossBrowser(request):
    return request.param
