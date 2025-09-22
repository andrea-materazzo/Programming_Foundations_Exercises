# Design Exercise 1: Turtle Graphics - Diamond Pattern
#
# Task: Use turtle graphics to draw a pattern of two diamonds.
import turtle
#
# Requirements:
# 1. Import the turtle module
# 2. Hide the turtle cursor
# 3. Set the fill color to blue
# 4. Draw the first diamond:
#    - Start at current position
#    - Turn left 135 degrees
#    - Move forward 100 units
#    - Turn left 90 degrees
#    - Move forward 100 units
#    - Turn left 90 degrees
#    - Move forward 100 units
#    - Turn left 90 degrees
#    - Move forward 100 units
# 5. Draw the second diamond:
#    - Move forward 100 units
#    - Turn right 90 degrees
#    - Move forward 100 units
#    - Turn right 90 degrees
#    - Move forward 100 units
#    - Turn right 90 degrees
#    - Move forward 100 units
#
# Note: Use begin_fill() and end_fill() to fill the shapes with color
#
# Expected result: Two blue diamond shapes drawn on the screen
turtle.hideturtle()
turtle.pencolor('blue')
turtle.left(135)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.done()
