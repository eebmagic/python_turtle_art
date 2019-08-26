import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Gray")


def spiral(inputLen):
	if inputLen <= 10:
		t.right(90)
	else:
		t.fd(inputLen)
		t.left(90)
		spiral(inputLen - 10)
		t.back(inputLen)
		t.right(90)


t.speed('fastest')
t.pensize(5)
for i in range(8):
	t.left(45)
	spiral(100)

t.hideturtle()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="spirals.eps")
turtle.done()
