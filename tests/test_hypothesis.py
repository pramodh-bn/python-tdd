from hypothesis import given
import hypothesis.strategies as st

from blog.util import increment

@given(st.integers())
def test_add_one(num):
    assert increment(num) == num + 1

