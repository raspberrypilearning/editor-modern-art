<h2 class="c-project-heading--task">Turn the colour code into a function</h2>

--- task ---
Create a function to set a random turtle colour.
--- /task ---

Writing the same code again and again is slow and hard to read.  
You can group often repeated code together in a *function* and run it whenever you need it.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-11,13
---

from turtle import *
from random import *

colormode(255)

def randomcolour(): # define the function - make sure the next lines are indented!
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

randomcolour()
shape("turtle")

--- /code ---
</div>

<div class="c-project-output">
<pre>The turtle is still a random colour, but the code is clearer.</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If your turtle is black, check that you have *called* the function with `randomcolour()` at the bottom

</div>
