import turtle
import math

turtle.pensize(10)

# Make a circle filled with black
turtle.color("black")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

# Move the turtle to the point (-80, 80)
turtle.penup()
turtle.setposition(-80, 150)

# Draw a line from the current position to (80, 80)
dx = 80 - (-80)
dy = 150 - 150
length = math.sqrt((dx * dx) + (dy * dy))

turtle.pendown()
turtle.forward(length)

# Move the turtle to the position (0, 150)
turtle.penup()
turtle.setposition(0, 150)

# Draw a line connecting the circle and the line
turtle.setheading(270)
turtle.pendown()
turtle.forward(15)

# Draw the legs of the helicopter
turtle.pensize(15)
turtle.penup()
turtle.setposition(-40, -10)
turtle.setheading(230)
turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.setposition(40, -10)
turtle.setheading(310)
turtle.pendown()
turtle.forward(25)

# Draw the partitions of the helicopter icon
turtle.penup()
turtle.setposition(-60, 55)
turtle.setheading(0)
turtle.pendown()
turtle.pencolor("white")
turtle.forward(120)

turtle.penup()
turtle.setposition(0, 120)
turtle.setheading(270)
turtle.pendown()
turtle.forward(60)
turtle.hideturtle()

turtle.done()
