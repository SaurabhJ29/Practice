import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])


for ele in a:
    for element in b:
        if ele == element:
            c = np.delete(a, ele)


print(c)
