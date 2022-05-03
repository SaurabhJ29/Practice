#class is a new type that may not be available/inbuilt in the language itself such as
#numbers, strings, Boolens, lists, dictionaries etc.
# from dis import dis
import math as m

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        length = m.sqrt((self.x)*(self.x) + (self.y)*(self.y))
        return length
        # print("The length of the point from the origin is: ", dist)


    def slope(self):
        slope = m.atan((self.y)/(self.x))
        return slope
        # print("The slope of the point w.r.t origin is: ", slope)

Cord_A = Coordinate(5, 10)
Cord_B = Coordinate(3, 4)

B = Coordinate.length(Cord_B)
print("The length of line B is: " B)
# Cord_A.length()
# Cord.y = 10
print("The length of the point from the origin is: ", Cord_A.length())
print("The slope of the point w.r.t x axis, with origin as the other point in radian is: ", Cord_B.slope())


# class Employee:
#     def __init__(self, first, last, pay):    #kind of constructor
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@id.com'

    
#     def fullname(self):
#         return ('{} {}'.format(self.first, self.last))


# emp_1 = Employee('Saurabh', 'Jain', 0)
# emp_2 = Employee('Rishabh', 'Jain', 100000)

# print(emp_1.fullname())
# print(emp_2.fullname())


# class and instance of a class
# instance variable contains data that is unique to each existence
# 
#
# class variables
# 