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


def main() -> None:
    """Main routine."""
    my_point: Point = Point(1.0, 1.0)

    my_point.x = 1.0
    my_point.y = 1.0

    print(my_point)
    print(my_point.x)
    print(my_point.y)

    my_point.scale_by(7)
    print(my_point.x)
    print(my_point.y)

    second_point: Point = Point(1.0, 1.0)
    print(second_point.scale(10).x)
    print(second_point.scale(10).y)


if __name__ == "__main__":
    main()
