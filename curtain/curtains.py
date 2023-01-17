import turtle
import random
from tkinter import *


def build(length, height, amp, prob):
    startRow = [0] * length
    out = [startRow]

    for i in range(height):
        new = []
        oldRow = out[-1]
        for x in range(length):
            if random.random() < prob:
                new.append(random.randint(0, amp) + out[i][x])
            else:
                new.append(out[i][x])
                # new.append(oldRow[x])
        out.append(new)

    return out


if __name__ == "__main__":
    w, h = 100, 300
    amp = 1
    prob = 0.2
    arr = build(w, h, amp, prob)

    screen = turtle.Screen()
    # screen.setup(1200, 800)
    screenWidth = 800
    screenHeight = 3 * screenWidth
    screen.setup(screenWidth, screenHeight)
    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()

    x_spacing = w / 10
    y_spacing = 2
    
    x_adj = 500
    y_adj = 350
    t.penup()

    for r_ind, row in enumerate(arr):
        y = r_ind * y_spacing
        for c_ind, cell in enumerate(row):
            x = c_ind * x_spacing

            t.goto(x - x_adj, -(y + cell - y_adj))
            t.pendown()

        t.penup()
        t.hideturtle()
    turtle.update()
    name = f"samples/canvas_output.eps"
    print(f"saving with name: {name}")
    screen.getcanvas().postscript(file=name)


    turtle.update()
    # input("press enter to export canvas as .eps files:... ")
    
    # ts = turtle.getscreen()
    # ts.getcanvas().postscript(file="samples/curtains.eps")

    turtle.done()