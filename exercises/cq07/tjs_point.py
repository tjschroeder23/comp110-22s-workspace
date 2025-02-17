"""Challenge Question 7 on Creating A Class called Point."""

from __future__ import annotations


class Point:
    """New class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My Point Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale and change self."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scale and return point without changing original."""
        return_point: Point = Point(self.x * factor, self.y * factor)
        return return_point
    
    def __str__(self) -> str:
        """Overload str magic method to print a Point object in a user readable fashion."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Scale and return point without changing original by overloading magic method multiplication."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Add a value to each x,y pair in point by overloading magic method addition."""
        return Point(self.x + factor, self.y + factor)
        

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

    print(second_point)
    print(second_point + 33.2)
    print(second_point * 7)


if __name__ == "__main__":
    main()
