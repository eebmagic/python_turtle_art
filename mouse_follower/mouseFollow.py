import turtle
import time
import pyautogui as gui
'''turtle screens can only get mouse coordinates on clicks
so I use pytautogui to constantly check the current mouse position'''

t = turtle.Turtle()
# Check that this is necessary later....
screen = turtle.Screen()
t.hideturtle()
t.speed('fastest')
t.pensize(3)

'''
These variables account for the difference between
the pyautogui mouse positon and the turtle position
You may have to tweak them to be more precise for your system'''
XDiffAccount = 644
YDiffAcccount = -425


def clickFunc(x, y):
	print("CLICKED")
	t.clear()
	t.pensize(1)


# Default start positon to define var for later use
lastMousePosition = (0, 0)

while True:
	# Clear and reset turtle on click
	screen.onclick(clickFunc)

	if gui.position() == lastMousePosition:
		t.pensize(t.pensize() + 1.2)
	else:
		shrinkAmount = 1.1
		if t.pensize() > shrinkAmount:
			t.pensize(t.pensize() - shrinkAmount)
		if t.pensize() == 1:
			t.pensize(1)

	# Move turtle to mouse with X & Y adjustments
	t.goto(gui.position()[0] - XDiffAccount, -(gui.position()[1]) - YDiffAcccount)

	# Get last mouse positon
	lastMousePosition = gui.position()
	time.sleep(0.005)
