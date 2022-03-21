"""Turtle tutorial practice."""

from random import randint
from turtle import Turtle, colormode, done

colormode(255)

leo: Turtle = Turtle()
bob: Turtle = Turtle()


leo.pencolor("blue")
leo.fillcolor(32, 136, 128)

side_length: float = 200

leo.penup()
leo.goto(-(side_length / 2), -(side_length / 2))
leo.pendown()
leo.speed(300)
leo.begin_fill()
i: int = 0
while (i < 5):
    leo.forward(side_length)
    leo.left(72)
    i = i + 1
leo.end_fill()
leo.ht()

bob.speed(100)
z: int = 0
while (z < 20):
    bob.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    bob.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    bob.begin_fill()
    i: int = 0
    side_length *= .90
    bob.penup()
    bob.goto(-(side_length / 2), -(side_length / 2))
    bob.pendown()
    while (i < 5):
        bob.forward(side_length)
        # bob.left(72)
        bob.left(73)
        i += 1
    z += 1
    # bob.left(randint(-20, 20))
    # bob.left(18)
    bob.end_fill()
bob.ht()


done()
