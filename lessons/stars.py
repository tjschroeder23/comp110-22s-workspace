
from turtle import Turtle, colormode, done, tracer, update, bgcolor, screensize
colormode(255)

white_star: Turtle = Turtle()
white_star.color("white")


def stars(star: Turtle, num_stars: int) -> None:
    side_length: float = 50
    star.ht()
    x: int = 10
    y: int = 10
    z: int = 0
    while z < num_stars:
        star.penup()
        star.goto(x, y)
        star.setheading(0)
        star.pendown()
        star.speed(0)
        star.begin_fill()
        five_star(star, side_length)
        star.end_fill()
        z += 1
    return


def five_star(st: Turtle, length: float):
    i: int = 0
    while (i < 5):
            st.forward(length)
            st.left(144)
            i += 1
    return


    