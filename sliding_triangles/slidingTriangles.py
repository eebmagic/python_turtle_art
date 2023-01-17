import turtle
import time

t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()
t.penup()
t.goto(180, 0)
t.pendown()

# SETTINGS #
base = 100
total = 130
side = total - base
angle = 15

# Dont show turtle movements until done
turtle.tracer(0, 0)

loop = True
while loop:
	t.fd(base)
	t.left(180)
	t.right(angle)
	t.fd(side)
	t.goto(180, 0)
	t.seth(0)
	print("angle: " + str(angle))
	base -= 5
	side = total - base
	angle += 5

	if angle >= 900:
		loop = False

# Display all new lines
turtle.update()
# turtle.done()

input("Press a button")
## SAVE
ts = turtle.getscreen()
ts.getcanvas().postscript(file="script_output.eps")