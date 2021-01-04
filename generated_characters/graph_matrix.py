import turtle
import math

turtle.bgcolor('black')
t = turtle.Turtle()
t.hideturtle()
t.pencolor('white')
t.speed('fastest')
turtle.tracer(0, 0)

def transform(point, origin):
    x, y = point
    a, b = origin
    return (x+a, y+b)

def draw_connection(a, b, origin=(0, 0)):
    # print(f'Drawing connection {a} -> {b}')
    a = transform(a, origin)
    b = transform(b, origin)
    t.penup()
    t.goto(a)
    t.pendown()
    t.goto(b)

def graph(matrix, scale=10, origin=(0, 0)):
    assert len(matrix) == len(matrix[0]), 'matrix must be square'

    width = math.sqrt(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            value = matrix[i][j]
            if value == True:
                a = ((i % width) * scale * (2/3), (i // width) * scale)
                b = ((j % width) * scale * (2/3), (j // width) * scale)
                draw_connection(a, b, origin=origin)



if __name__ == '__main__':
    from build_matrix import build

    size = 20
    count = 7
    for x in range(count):
        for y in range(count):
            m = build(9)
            o = (x*size*4 - size*count*2, y*size*4 - size*count*2)
            graph(m, scale=size, origin=o)

    turtle.update()
    turtle.done()