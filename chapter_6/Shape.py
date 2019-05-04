#!/usr/bin/env python3
# Copyright (c) 2019 Alex Vakhov. All rights reserved.
"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """

        self.x = x
        self.y = y

    @property
    def distance_from_origin(self) -> math.hypot:
        """The distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin
        5.0
        """

        return math.hypot(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '{0.__class__.__name__}({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!r}, {0.y!r})'.format(self)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    @property
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin - self.radius)

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def radius(self):
        """
        The circle's radius

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle.radius = 6
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius

    def __eq__(self, other):
        return self.radius == other.radius and super(Circle, self).__eq__(other)

    def __repr__(self):
        return '{0.__class__.__name__}({0.radius!r}, {0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return repr(self)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    a = Point()
    print(repr(a))
    print(a)

    b = Point(3, 4)
    print(b)
    b.distance_from_origin
    b.x = -19
    print(b)
    print(a == b, a != b)

    c = Circle(radius=6)
    print(c == c)

    p = Point(28, 45)
    c = Circle(5, 28, 45)
    print(p.distance_from_origin)
    print(c.distance_from_origin)
