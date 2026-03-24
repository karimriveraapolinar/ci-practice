import pytest
from score import Score

def test_add_points():
    s = Score()
    s.add_points(10)
    assert s.points == 10

def test_reset():
    s = Score()
    s.add_points(5)
    s.reset()
    assert s.points == 0

def test_negative_raises():
    s = Score()
    with pytest.raises(ValueError):
        s.add_points(-1)