import turtle
import random

print("")

# SHARED SETTINGS
speed = 4
size = 3

# TURTLE VARS #
t = turtle.Turtle()
t.hideturtle()
t.speed(speed)

t.pensize(size)
t.color("green")


''' USER SETTINGS '''
# This is resolution of my screen, you may have to tweak this for your system
run_width, run_height = 1280, 800
runWithTrail = input("Would you like to run with Trail? (y/N): ")


# TRAILING TURTLE #

trail = turtle.Turtle()
trail.hideturtle()
trail.speed(speed)

trail.pensize(size / 4.5)
trail.color("white")

# SCREEN COLORS #
screen = turtle.Screen()
screen.bgcolor("black")

# TURTLE MOVEMENT #
minDistance = 15
maxDistace = 300

# SIDE LIMITS #
screen.setup(width=run_width, height=run_height)

rightLimit = (run_width / 2)
leftLimit = -(run_width / 2)
topLimit = (run_height / 2)
bottomLimit = -(run_height / 2)

margin = maxDistace - minDistance

cycleLimit = 10


# turn a random direction
def turn():
	fromX = (90, 270, 45, 225)
	fromY = (0, 180, 45, 225)
	fromZ = (0, 90, 180, 270)

	newX = random.choice(fromX)
	newY = random.choice(fromY)
	newZ = random.choice(fromZ)

	# on X axis
	if t.heading() in [0, 180]:
		t.seth(newX)
		if runWithTrail == "Y" or runWithTrail == "y":
			trail.seth(newX)

	# on Y axis
	elif t.heading() in [90, 270]:
		t.seth(newY)
		if runWithTrail == "Y" or runWithTrail == "y":
			trail.seth(newY)

	# on Z axis
	elif t.heading() in [45, 225]:
		t.seth(newZ)
		if runWithTrail == "Y" or runWithTrail == "y":
			trail.seth(newZ)


def move():
	distance = random.randint(minDistance, maxDistace)
	t.fd(distance)
	if runWithTrail == "Y" or runWithTrail == "y":
		trail.fd(distance)
	else:
		pass


def resetXY():
	t.up()
	t.setx(0)
	t.sety(0)
	t.down()
	global resetCount
	resetCount += 1
	if runWithTrail == "Y" or runWithTrail == "y":
		trail.up()
		trail.setx(0)
		trail.sety(0)
		trail.down()


def resets():
	# RESETS TO BE EXECUTED WHEN PAST LIMIT & START #
	resetXY()

	# Wipe Board
	global resetCount
	if resetCount > cycleLimit:
		t.clear()
		trail.clear()
		resetXY()
		resetCount = 0
		print("BOARD WIPED")


def checkLimits():
	if t.xcor() > rightLimit:
		pastRight = True
		pastLimit = True
		print("\n~~~RIGHT was triggered~~~")
		resets()

	if t.xcor() < leftLimit:
		pastLeft = True
		pastLimit = True
		print("\n~~~LEFT was triggered~~~")
		resets()

	if t.ycor() > topLimit:
		pastTop = True
		pastLimit = True
		print("\n~~~TOP was triggered~~~")
		resets()

	if t.ycor() < bottomLimit:
		pastBotom = True
		pastLimit = True
		print("\n~~~BOTTOM was triggered~~~")
		resets()


resetCount = 0
resets()
print("###START###")
print(t.pos())
print("")

while KeyboardInterrupt:
	valid_inputs = ['Y', 'y', 'N', 'n', '']
	while runWithTrail in valid_inputs:
		# move random distance and turn left or right
		turn()
		move()

		# console checks #
		print("heading:	" + str(t.heading()))
		print("position:	" + str(t.pos()))

		# if turtle has passed a side
		checkLimits()

		print("")

	else:
		print("Response must be 'Y' or 'N'")
		runWithTrail = input("Would you like to run with Trail? (y/N): ")

turtle.mainloop()
