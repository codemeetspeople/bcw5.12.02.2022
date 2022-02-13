import pytest
from math import sqrt

from point.point import Point


def test_constructor():
    a = Point()
    b = Point(1, 10)

    assert a.x == 0.0
    assert a.y == 0.0
    assert b.x == 1.0
    assert b.y == 10.0


def test_constructor_exceptions():
    with pytest.raises(ValueError):
        Point('error', 'fail')

    with pytest.raises(TypeError):
        Point(Point(), Point())


def test_setters():
    point = Point()

    assert point.x == 0.0
    assert point.y == 0.0

    point.x = -10
    point.y = 5

    assert point.x == -10.0
    assert point.y == 5.0


def test_setters_exceptions():
    point = Point()

    with pytest.raises(ValueError):
        point.x = 'error'

    with pytest.raises(TypeError):
        point.y = Point()


def test_str_representation():
    out = str(Point())
    assert out == '(0.0, 0.0)'


def test_operators():
    a = Point()
    b = Point(1, 2)

    assert a != b
    assert not a == b


def test_point_distance():
    a = Point()
    b = Point(1, 1)

    assert a.distance(b) == sqrt(2)
