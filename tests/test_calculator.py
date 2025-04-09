import pytest
from calculator import add


@pytest.fixture
def numbers():
    return (2, 3)


def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 5


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def test_add_multiple(a, b, expected):
    assert add(a, b) == expected