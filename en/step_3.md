<h2 class="c-project-heading--task">Make the colour random</h2>

--- task ---
Use random numbers to change the turtle’s colour each time.
--- /task ---

Instead of choosing the colour yourself, you can let Python choose random values between 0 and 255 using `randint(0, 255)`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---

from turtle import *
from random import *

colormode(255)

color(randint(0, 255), randint(0, 255), randint(0, 255))
shape("turtle")

--- /code ---
</div>

<div class="c-project-output">
<pre>The turtle changes colour every time you click Run.</pre>
</div>
