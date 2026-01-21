<style>
.rpf-tip{
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted currentColor;
  cursor: help;
}

.rpf-tip::after{
  content: attr(data-tip);
  position: absolute;
  left: 0;
  bottom: 125%;

  width: max-content;
  max-width: 38ch;
  white-space: normal;

  padding: .5em .6em;
  font-size: .85em;
  line-height: 1.25;

  background: #111;
  color: #fff;
  border-radius: .35em;

  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  z-index: 9999;
}

.rpf-tip::before{
  content: "";
  position: absolute;
  left: 1em;
  bottom: 115%;
  border: .4em solid transparent;
  border-top-color: #111;

  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  z-index: 9999;
}

.rpf-tip:hover::after,
.rpf-tip:focus::after,
.rpf-tip:hover::before,
.rpf-tip:focus::before{
  opacity: 1;
  visibility: visible;
}
</style>

<h2 class="c-project-heading--task">Set the turtle colour</h2>

<div class="c-project-code">
--- task ---
Set the turtle’s colour using 
<span class="rpf-tip" tabindex="0"
      data-tip="RGB colours are made by mixing Red, Green, and Blue light. Each value controls how strong that colour is: 0 means none, 255 means maximum. Different combinations create different colours.">
  red, green, and blue values
</span>.  
Each colour value can be between `0` and `255`.
--- /task ---

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

colormode(255)                # Use RGB colour values from 0–255

color(255, 0, 0)              # Set colour value to 255,0,0 = Red
shape("turtle")               # Set shape to Turtle

--- /code ---
</div>

--- task ---

**Test**: Run your code and check the output.  
A turtle should appear on the screen in the colour you set using the RGB values.

--- /task ---

<div class="c-project-output">
<pre><div class="c-project-output">
  <img src="images/redturtle.png"
       alt="Three turtles shown after different runs of the program, each appearing in a different random colour."></pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Red, green, and blue (RGB) values range from 0 to 255 – using numbers outside this range will give an error
- Changing the numbers changes the colour – have a play with them and run the code again!

</div>
