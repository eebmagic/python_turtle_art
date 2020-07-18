import turtle
import math

t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()
t.right(90)

# turtle.bgcolor("brown")
# turtle.bgcolor("#FAD0C0")
turtle.bgcolor("#E0B2A1")

wn = turtle.Screen()
wn.setup(width=1000, height=1400)
wn.title("complex_web")


iterations = 1000
fd_mult = 0.5
# angle_mult = math.pi * 4
angle_mult = 50
name_num_len = 4

i = 0
while i < iterations:
    t.fd(i * fd_mult)
    angle = i * angle_mult

    if i % 2 == 0:
        angle = -angle

    t.left(angle)

    if i % 5 == 0:
        ts = turtle.getscreen()
        file_out_name = f"output/out_{str(i).zfill(name_num_len)}.eps"
        print(file_out_name)
        # ts.getcanvas().postscript(file=file_out_name)

    i += 1


print("DONE")
turtle.done()