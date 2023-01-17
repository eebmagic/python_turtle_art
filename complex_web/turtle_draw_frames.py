import turtle
import math

wn = turtle.Screen()
h = 800
w = 3 * h
wn.setup(width=w, height=h)
wn.title(f"w: {w}, h: {h}")

t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()

# turtle.bgcolor("brown")
# turtle.bgcolor("#FAD0C0")
turtle.bgcolor("#E0B2A1")



iterations = 1500
fd_mult = 0.5
# angle_mult = math.pi * 4
angle_mult = 50
name_num_len = 4

turtle.tracer(0, 0)

i = 0
while i < iterations:
    t.fd(i * fd_mult)
    angle = i * angle_mult

    if i % 2 == 0:
        angle = -angle

    t.left(angle)

    i += 1

turtle.update()
ts = turtle.getscreen()
file_out_name = f"output/out_{i:04}.eps"
wn.getcanvas().postscript(file=file_out_name)
print(file_out_name)

print("DONE")
turtle.done()