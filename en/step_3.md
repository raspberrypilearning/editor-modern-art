## Turn the colour code into a function

Create a function to set a random turtle colour.

Writing the same code again and again is slow and hard to read.
You can group often repeated code together in a **function** and run it whenever you need it.

```python filename="main.py" line_numbers="true" line_number_start="1" line_highlights="6-12"

from turtle import *          # Import turtle graphics tools
from random import *          # Import random number tools

colormode(255)                # Use RGB colour values from 0-255

def randomcolour():           # Function to set a random turtle colour
    red = randint(0, 255)           # Pick a random red value
    green = randint(0, 255)         # Pick a random green value
    blue = randint(0, 255)          # Pick a random blue value
    color(red, green, blue)         # Set the turtle colour

randomcolour()                # Choose a random colour
shape("turtle")               # Set shape to Turtle

```

> [!DEBUG]
>
> - If your turtle is black, check that you have **called** the function with `randomcolour()` at the bottom

## Now run your code

The turtle should still appear in a random colour, even though the colour code is now inside a function.

![Three turtles shown after different runs of the program, each appearing in a different random colour.](images/randomcolours.png)
