import turtle


def tri(turt, size=100):
	for i in range(3):
		turt.fd(size)
		turt.left(120)


def drawThatShape(turt):
	turt.begin_fill()
	for i in range(3):
		lastDistance = 100 + 20 * i
		tri(turt, lastDistance)
	turt.end_fill()

	turt.fd(lastDistance + 20)
	turt.left(120)
	turt.fd(lastDistance + 20)
	turt.hideturtle()


size = 2.5

t1 = turtle.Turtle()
t1.hideturtle()
t1.pensize(size)
t1.speed('fastest')

t2 = turtle.Turtle()
t2.hideturtle()
t2.pensize(size)
t2.speed('fastest')

colorSetting = (0.9, 0.3, 0.4)

screen = turtle.Screen()
screen.bgcolor(colorSetting)


drawThatShape(t1)
t2.fd(100)
t2.left(180)
drawThatShape(t2)


t1.hideturtle()
turtle.done()
