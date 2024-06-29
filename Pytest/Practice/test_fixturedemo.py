import pytest


@pytest.mark.usefixtures("setup")
class Testexample:

    def test_after_set_up(self):
        print("I will be executed next")


    def test_after_set_up1(self):
        print("I will be executed next - setup1")


    def test_after_set_up2(self):
        print("I will be executed next - setup2")


    def test_after_set_up3(self):
        print("I will be executed next - setup3")
