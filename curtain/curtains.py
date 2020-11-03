import turtle
import random


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
    w, h = 100, 200
    amp = 1
    prob = 0.5
    arr = build(w, h, amp, prob)

    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()

    x_spacing = w / 15
    y_spacing = 3
    
    x_adj = 400
    y_adj = 350
    t.penup()

    for r_ind, row in enumerate(arr):
        y = r_ind * y_spacing
        for c_ind, cell in enumerate(row):
            x = c_ind * x_spacing

            t.goto(x - x_adj, -(y + cell - y_adj))
            t.pendown()

        t.penup()

    turtle.update()
    turtle.done()