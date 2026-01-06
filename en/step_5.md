<h2 class="c-project-heading--task">Move the turtle to a random place</h2>

--- task ---
Move the turtle to a random position on the screen.
--- /task ---

The centre of the screen is at `(0, 0)`.  
You can move the turtle to a random x and y position.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 13-19,21-23
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

randomcolour()
randomplace()
shape("turtle")

--- /code ---
</div>

<div class="c-project-output">
<pre>The turtle appears in a random place and colour.</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If lines appear, check `penup()` and `pendown()`
- If the cursor is an arrow, check where `shape("turtle")` is called

</div>
