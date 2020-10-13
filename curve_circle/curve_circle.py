import turtle
import random
import math

def shape(x, size):
    for i in range(0, size):
        x.fd(size/2)
        x.left(180/size)

    for i in range(0, size):
        x.fd(size/2)
        x.right(180/size)

# Turtle settings
t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
turtle.tracer(0, 0)


# Set Constants
length = 180 + 90
startShift = 0
count = 100
shapeSize = 20
turn = math.ceil((length) / count)

# Main Loop
for i in range(startShift, startShift + length, turn):
    # t.left(i * turn + startShift)
    t.left(i)
    shape(t, shapeSize)

    t.penup()
    t.home()
    t.pendown()

# Show drawing
turtle.update()
turtle.done()