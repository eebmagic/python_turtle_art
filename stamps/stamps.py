import turtle

t = turtle.Turtle()
screen = turtle.Screen()
############## Settings ###################
t.pensize(5)
t.speed('fastest')
t.hideturtle()
###########################################

drawing = False
squareSize = 50
turtle.tracer(0,0)

def teleport(x, y):
	t.penup()
	t.setpos(x-squareSize/2, y-squareSize/2)
	t.pendown()

def square(x, y):
	global drawing
	drawing = True
	for i in range(4):
		t.fd(squareSize)
		t.left(90)
	drawing = False
	turtle.update()

def trySquare(x, y):
	global drawing
	if drawing == False:
		teleport(x, y)
		square(1, 1)

userQuit = None

while userQuit == None:
	screen.onclick(trySquare)

############### END ######################
	userQuit = input('Press Enter to Quit:')
	if userQuit == '':
		quit()