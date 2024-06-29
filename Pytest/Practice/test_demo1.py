import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstprogram():
    msg = "hi"
    assert msg == "hi", ("Test Failed")


@pytest.mark.xfail
def test_secondprogram():
    msg = "hi"
    assert msg == "hello", "Test Failed"


@pytest.mark.usefixtures()
def test_cross_Browser(crossBrowser):
    print("Inside Test CrossBrowser")
    print(crossBrowser[0][1])
    print(crossBrowser[0][0])
    print("Test CrossBrowser ends")

