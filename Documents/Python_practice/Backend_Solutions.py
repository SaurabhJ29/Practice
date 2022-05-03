import numpy as np
a = np.array([[-3, 2, 1], [1, -1, 0], [-1, 10, 1]])
b = np.array([2, 4, -1])
from scipy import linalg
x = linalg.solve(a, b)

print(x)