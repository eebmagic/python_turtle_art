import turtle

t = turtle.Turtle()
# t.speed("fastest")

angle = 45 / 2
iterations = 25
adjust_angle = 5
turts = 360 // adjust_angle

for x in range(turts):
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(x * adjust_angle)
    for i in range(iterations):
        t.fd(100)
        t.left(i * angle)

    t.hideturtle()



turtle.done()