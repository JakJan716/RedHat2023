import pytest

@pytest.mark.parametrize(
"test_in, expected", 
[(3, 4), (5, 6), (6, 7)],
)

def func(test_in):
    return test_in + 1


def test_answer(test_in, expected):
    assert func(test_in) == expected