<h2 class="c-project-heading--task">Set the turtle colour</h2>

--- task ---
Set the turtle’s colour using red, green, and blue values.
--- /task ---

Set the turtle colour by choosing how much red, green, and blue you want.  
Each value can be between `0` and `255`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---

from turtle import *
from random import *

colormode(255)

color(255, 0, 0)
shape("turtle")

--- /code ---
</div>

<div class="c-project-output">
<pre>A turtle appears in the colour you chose.</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Red, green, and blue (RGB) values range from 0 to 255 - using numbers outside this range will give an error
- Changing the numbers changes the colour - have a play with them and run the code again!

</div>
