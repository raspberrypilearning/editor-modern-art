<h2 class="c-project-heading--task">Draw modern art with rectangles</h2>

--- task ---
Replace turtle stamps with randomly sized rectangles.
--- /task ---

You can turn your turtle art into modern art by drawing rectangles instead.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 27-44,46-47
---

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
    pendown()

# Comment out the turtle stamp code by placing hashtags at the beginning of each line you don't want
# shape("turtle")
# for i in range(30):
#     randomcolour()
#     randomplace()
#     stamp()

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

for i in range(20):
    draw_rectangle()

--- /code ---
</div>

<div class="c-project-output">
<pre>A piece of modern art made from coloured rectangles appears.</pre>
</div>
