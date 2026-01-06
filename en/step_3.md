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

from turtle import *          # Import turtle graphics tools
from random import *          # Import random number tools

colormode(255)                # Use RGB colour values from 0–255

color(randint(0, 255), randint(0, 255), randint(0, 255))        # Set colour values to three random numbers
shape("turtle")               # Set shape to Turtle

--- /code ---

--- task ---

**Test**: Run your code several times.  
Each time you run the code, the turtle should appear in a different colour.

--- /task ---


</div>

<div class="c-project-output">
  <img src="images/randomcolours.png"
       alt="Three turtles shown after different runs of the program, each appearing in a different random colour.">
</div>
