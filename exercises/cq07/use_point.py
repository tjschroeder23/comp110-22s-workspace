"""Using and importing the Point Class and methods."""

from exercises.cq07.tjs_point import Point


My_point: Point = Point(1.0, 1.0)

My_point.x = 1.0
My_point.y = 1.0

# print(My_point)
print(My_point.x)
print(My_point.y)

My_point.scale_by(7)
print(My_point.x)
print(My_point.y)

Second_point: Point = Point(1.0, 1.0)
print(Second_point.scale(10).x)
print(Second_point.scale(10).y)
