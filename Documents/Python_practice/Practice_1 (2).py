# a=1
# b=2
# def func():
#     global b
#     b = a+b
# func()
# print(b)

# def inc(a,b=1):
#     return(a+b)
# a=inc(1)
# a=inc(a,a)
# print(a)

# from this import d


# data = [2, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# def Sum10th(data):
#   sum=0
#   for i,d in enumerate(data):
#     if (i % 10 == 0): return sum
#     sum=sum+d

# print(Sum10th(data))

# try:
#     x = int(input("Enter the age of a person: "))
#     print("Age of the person is ", x)
# except ValueError:
#     print("Invalid Value")


# try:
#     age = int(input("Age: "))
#     income = 5000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be 0 for a salaried person")
# except ValueError:
#     print("Invalid Value")


import math
epsilon = 0.000001

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def dist_to_point(self, other):
        'Compute the Euclidean distance between two Point objects'
        delta_x = self._x - other._x
        delta_y = self._y - other._y
        return (delta_x ** 2 + delta_y ** 2) ** 0.5


point_abc = Point(1,2)
point_def = Point(3,4)
point_abc.dist_to_point(point_def)