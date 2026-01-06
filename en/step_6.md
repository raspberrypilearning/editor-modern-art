<h2 class="c-project-heading--task">Create turtle stamp art</h2>

--- task ---
Use stamps and a loop to create turtle art.
--- /task ---

The `stamp()` command leaves a copy of the turtle on the screen.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 21-25
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

shape("turtle")

for i in range(30):
    randomcolour()
    randomplace()
    stamp()

--- /code ---
</div>

<div class="c-project-output">
<pre>Lots of turtles are stamped in different places and colours.</pre>
</div>
