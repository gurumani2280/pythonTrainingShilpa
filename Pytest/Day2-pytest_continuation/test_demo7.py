import pytest

# Arrange
@pytest.fixture
def fruit_bowl():
    return ["apple", "banana","Mango"]


def test_fruit_salad(fruit_bowl):
    # Act
    print("Fruit Bowl",fruit_bowl)
    list1 = fruit_bowl
    print(list1[0:2])

