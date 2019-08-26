import turtle

t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor('sandy brown')

# SETTINGS #
RAY_LEN = 350
t.pensize(1.2)


# DRAW #
t.left(90)
t.fd(RAY_LEN)

lastPos = 5
lastAngle = 90

for i in range(59):
	t.penup()

	# Position
	t.goto(lastPos, 0)
	if lastPos > 0:
		pass
	else:
		lastPos -= 5
	lastPos *= -1

	# Orient
	if t.pos()[0] > 0:
		lastAngle += (5 * i)
	else:
		lastAngle += (5 * -i)
	t.seth(lastAngle)

	# Draw
	t.pendown()
	t.fd(RAY_LEN)

turtle.done()
