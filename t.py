import pandas as pd
import numpy as np

matrix = np.array([
    [1, 2, -1, 7],
    [0, -2, 4, 5],
    [3, -1, 8, 0],
    [1, 2, -1, 7]
])

x = np.linalg.det(matrix)
print(x)

a = np.array([12, 56, 23, 65, 74])
b = np.array([100, 33, 12, 7, 54])

c = (a - b)

z = sum([abs(i) for i in c]) / 5
print(z)
