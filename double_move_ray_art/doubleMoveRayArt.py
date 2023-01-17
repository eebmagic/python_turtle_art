import turtle
import random
import time

colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']


class ray():
	def __init__(self, pensize):
		self.turt = turtle.Turtle()
		index = random.randint(0, len(colors) - 1)
		self.turt.pencolor(colors[index])
		self.turt.speed('fastest')
		self.turt.hideturtle()
		self.turt.pensize(pensize)

	def doubleMove(self):
		heading = random.randint(0, 360)
		self.turt.seth(heading)
		self.turt.fd(random.randint(15, 150))
		heading += random.randint(-35, 35)
		self.turt.seth(heading)
		self.turt.fd(random.randint(15, 150))


screen = turtle.Screen()
screen.bgcolor('light gray')

count = 0
size = 25
while True:
	try:
		count += 1
		if count % 5 == 0 and size != 1:
			size -= 1
		if size == 1:
			print("Only drawing small lines now")
		print("line size: " + str(size))

		newFormed = ray(size)
		newFormed.doubleMove()
		time.sleep(0.1)

	except KeyboardInterrupt:
		turtle.done()
