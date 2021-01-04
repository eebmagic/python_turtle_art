import numpy as np
import random

def add_connection(matrix, a, b):
    matrix[a][b] = True
    matrix[b][a] = True

    return matrix

def build(size: int, minimum=4, maximum=6):
    total = random.randint(minimum, maximum)

    m = np.full((size, size), False)

    for i in range(total):
        a = -1
        b = -1
        while a == b:
            a = random.randint(0, size-1)
            b = random.randint(0, size-1)

        m = add_connection(m, a, b)

    return m


if __name__ == '__main__':
    print(build(9))
