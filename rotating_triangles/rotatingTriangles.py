import turtle
from time import sleep
from math import sqrt


def triangle(turt):
	for i in range(3):
		turt.fd(armLength)
		turt.left(120)


def hex(turt):
	for i in range(6):
		triangle(turt)
		turt.left(60)


def setExtraPositions():
	zero.penup()
	zero.setpos(0, halfHeight)
	zero.pendown()
	zero.right(60)

	one.penup()
	one.setpos(-halfWidth, -halfHeight)
	one.pendown()
	one.left(60)

	two.penup()
	two.setpos(halfWidth, -halfHeight)
	two.pendown()
	two.right(180)


screen = turtle.Screen()
screen.bgcolor('light green')

zero = turtle.Turtle()
one = turtle.Turtle()
two = turtle.Turtle()

# GENERAL SETTINGS #
armLength = 200
halfWidth = armLength / 2
halfHeight = (halfWidth * sqrt(3)) / 2
speed = 'fastest'

# Apply Settings
extraTurtles = [zero, one, two]
for name in extraTurtles:
	name.speed(speed)
	name.hideturtle()
	name.pensize(5)

# CYCLES OPTION (Change this if you want)
count = 4

# START #
print("########## STARTING ##########")

# Move turtles for extra triangles
setExtraPositions()

for i in range(count):
	print(i)
	# Hexs
	for name in extraTurtles:
		hex(name)
		# name.left(15)
		name.seth((60 / count) * (i + 1))
		print(name.heading())


sleep(4)
turtle.done()
quit()
