from math import hypot


class Point:
    # __slots__ = ('_x', '_y')

    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def distance(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return hypot(self.x - other.x, self.y - other.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)


if __name__ == '__main__':  # pragma: no cover
    a = Point()
    b = Point(1, 1)

    if a == b:
        print(f'{a} == {b}')
    else:
        print(f'{a} != {b}')

    print(f'distance: {a.distance(b)}')
