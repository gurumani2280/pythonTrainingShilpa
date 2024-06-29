import pytest


@pytest.mark.usefixtures()
class Testexample2:
    def test_edit_profile(self,dataLoad):
        print(dataLoad[0])




