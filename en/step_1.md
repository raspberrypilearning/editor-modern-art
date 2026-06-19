<h2 class="c-project-heading--task">Set the turtle colour</h2>

Set the turtle's colour using red, green, and blue values.

RGB colours are made by mixing red, green, and blue light. Each value controls how strong that colour is: `0` means none and `255` means maximum. Different combinations create different colours.

Each colour value can be between `0` and `255`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---

from turtle import *          # Import turtle graphics tools
from random import *          # Import random number tools

colormode(255)                # Use RGB colour values from 0-255

color(255, 0, 0)              # Set colour value to 255,0,0 = Red
shape("turtle")               # Set shape to Turtle

--- /code ---
</div>

### Tip
<div class="c-project-callout c-project-callout--tip">

- Red, green, and blue (RGB) values range from 0 to 255. Using numbers outside this range will give an error.
- Changing the numbers changes the colour. Have a play with them and run the code again!

</div>

## Now run your code

A turtle should appear on the screen in the colour you set using the RGB values.

<div class="c-project-output">
  <img src="images/redturtle.png"
       alt="Three turtles shown after different runs of the program, each appearing in a different random colour.">
</div>
