"""Challenge Question 7 on Creating A Class called Point."""

from __future__ import annotations


class Point:
    """New class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """My Point Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Scale and change self."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scale and return point without changing original."""
        return_point: Point = Point(self.x * factor, self.y * factor)
        return return_point


My_point: Point = Point(1.0, 1.0)

My_point.x = 1.0
My_point.y = 1.0

# print(My_point)
# print(My_point.x)
# print(My_point.y)

# My_point.scale_by(7)
# print(My_point.x)
# print(My_point.y)
