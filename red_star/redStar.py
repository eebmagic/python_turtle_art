import turtle

SPEED_SETTING = 25

t = turtle.Turtle()
t.speed(SPEED_SETTING)
t.hideturtle()
t.speed("fastest")

t2 = turtle.Turtle()
t2.speed(SPEED_SETTING)
t2.hideturtle()
t2.speed("fastest")


# Initial Color Settings
r = 0.8
x = 0
tup = (r, x, x)
t.pensize(12)
t.pencolor(tup)
t2.pensize(12)
t2.pencolor(tup)

# misc vars
count = 0
starSize = 12

# Position Turtles
spread = starSize * 4.3
t.penup()
t.lt(90)
t.fd(spread)
t.pendown()
t2.penup()
t2.rt(90)
t2.fd(spread)
t2.pendown()


def drawToWhite(self):
	count = 0
	x = 0
	tup = (r, x, x)
	while count <= starSize:
		self.fd(10)
		x += (1 / starSize)
		self.pencolor(tup)
		tup = (r, x, x)

		count += 1


def drawToRed(self):
	count = starSize
	x = 1
	tup = (r, x, x)
	while count >= 0:
		self.fd(10)
		x -= (1 / starSize)
		self.pencolor(tup)
		tup = (r, x, x)

		count -= 1


while True:
	drawToWhite(t)
	drawToWhite(t2)
	t.rt(175)
	t2.rt(175)
	drawToRed(t)
	drawToRed(t2)
	adjustAngle = 13
	t.lt(175 - adjustAngle)
	t2.lt(175 - adjustAngle)
