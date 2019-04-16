#!/usr/bin/env python3
import math


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> math.hypot:
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Point({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!r}, {0.y!r})'.format(self)


if __name__ == '__main__':
    a = Point()
    print(repr(a))
    print(a)

    b = Point(3, 4)
    print(b)
    b.distance_from_origin()
    b.x = -19
    print(b)
    print(a == b, a != b)
