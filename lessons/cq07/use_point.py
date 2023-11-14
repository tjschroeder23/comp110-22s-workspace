"""Using and importing the Point Class and methods."""

from lessons.cq07.tjs_point import Point


My_point: Point = Point(2.0, 2.0)

My_point.x = 1.0
My_point.y = 1.0

print(My_point.x)
print(My_point.y)

My_point.scale_by(7)
print(My_point.x)
print(My_point.y)

Second_point: Point = Point(1.0, 1.0).scale(10)
print(Second_point.x)
print(Second_point.y)

third_point: Point = My_point.scale(10)
print(third_point.x)
print(third_point.y)
print(My_point.x)
print(My_point.y)
