import turtle
from time import time
start = time()

t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()

turtle.tracer(0, 0)

side = 1
for i in range(300):
	t.fd(side)
	side += 1
	t.left(55)

print(time() - start)
turtle.update()
turtle.done()
