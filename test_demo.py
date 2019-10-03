import pytest
import demo

def test_add():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    assert demo.add(3,4) == 7
    assert demo.add(1,9) == 10
    assert demo.add(2,4) == 6
