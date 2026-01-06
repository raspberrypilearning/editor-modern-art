from turtle import *
from random import *

colormode(255)


def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)


def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown


# Code to draw a random-sized rectangle
def draw_rectangle():
    speed(0)
    hideturtle()
    randomcolour()
    randomplace()
    length = randint(10, 100)
    height = randint(10, 100)
    begin_fill()
    for i in range(2):
        forward(length)
        right(90)
        forward(height)
        right(90)
    end_fill()


# shape("turtle")

# for i in range(30):
#    randomcolour()
#    randomplace()
#    stamp()

for i in range(20):
    draw_rectangle()
