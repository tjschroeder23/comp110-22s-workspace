"""Turtle scene.  Begals win superbowl with fireworks."""

__author__ = "tjschroeder23"

from random import randint
from turtle import Turtle, colormode, done, tracer, update, bgcolor, screensize
colormode(255)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    joe: Turtle = Turtle()
    bgcolor("black")
    screensize(1200, 700)
    joe.pencolor("black")
    joe.fillcolor(255, 130, 0)
    joe.pensize(2)
    joe.ht()
    
    sam: Turtle = Turtle()
    sam.pencolor("yellow")
    sam.fillcolor("blue")
    sam.pensize(2)
    sam.ht()

    backer: Turtle = Turtle()
    backer.pencolor("white")
    backer.fillcolor("green")
    backer.pensize(5)
    backer.ht()

    tracer(8, 0)
    football_field(backer, -500, -100)
    update()

    random_stars(joe, -500, -300, 0, 200, 15)
    random_stars(sam, 300, 500, 0, 200, 15)
    update()
    done()
    

def football_field(field: Turtle, x: float, y: float) -> None:
    field.pu()
    field.goto(x, y)
    field.speed(0)
    # field.setheading(0)
    field.pd()
    t: int = 0
    while t < 10:
        field.begin_fill()
        i: int = 0
        while i < 2:
            field.forward(100)
            field.left(90)
            field.forward(300)
            field.left(90)
            i += 1
        field.end_fill()
        field.forward(100)
        t += 1
    # return


def random_stars(star: Turtle, x1: int, x2: int, y1: int, y2: int, num_stars: int) -> None:
    side_length: float = 50
    star.ht()
    z: int = 0
    while z < num_stars:
        star.penup()
        star.goto(randint(x1, x2), randint(y1, y2))
        star.setheading(randint(0, 360))
        star.pendown()
        star.speed(0)
        star.begin_fill()
        i: int = 0
        while (i < 5):
            star.forward(side_length)
            star.left(144)
            i += 1
        star.end_fill()
        z += 1
    return


if __name__ == "__main__":
    main()
