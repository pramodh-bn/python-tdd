import pytest
from app.util import increment
from app.util import another_sum

@pytest.mark.parametrize(
    'number, result',
    [
        (-2, -1),
        (0, 1),
        (3, 4),
        (101234, 101235)
    ]
)
def test_increment(number, result):
    assert increment(number) == result

def test_another_sum():
    assert another_sum(3, 2) == 5