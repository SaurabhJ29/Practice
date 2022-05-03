import math as m
# import numpy as np

# def distance(p1, p2):
#     d = m.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0]**2))
#     return d

# def slope(p1, p2):
#     print(p2, p1)
#     print(p2[0], p1[0])
#     print("\nDifference is:", p2[0]-p1[0])
#     m = float((p2[1] - p1[1])/(p2[0]-p1[0]))
#     print("Slope of the line is:", m)
#     print("Type of slope of the line is: ", type(m))
#     return m


def line_check(strArray):
    print("Array is:", strArray)
    # print("First element of the array is:", strArray[0])
    # print("Second element of the array is:",strArray[1])
    p1 = strArray[0]
    # print("abcissa of point is:", p1[0])
    # print("The type of array element is:", type(p1[0]))
    p2 = strArray[1]
    p3 = strArray[2]

    # slope_line = float(slope(p1, p2))
    # print("Type of slope line is:", type(slope_line))
    # print("Slope is", slope)
    # c = p1[1]-slope_line*p1[0]
    # print("Intercept is", c)
    # y = slope*x+c
    # print("y =" , slope , "x +" , c)

    # if abs(slope_line) == abs(slope(p1, p3)):
        
        # d1 = distance(p1, p3)
        # d2 = distance(p2, p3)
        
        # print ("distance between point 1 and point 3 is", d1)
    #     # print ("distance between point 2 and point 3 is", d2)

    #     if p3[0]>p1[0]:
    #         if p3[0]>p2[0]:
    #             print("Right Side")
    #         else:
    #             print("Neither")
    #     else:
    #         print("left side")

    # else:
    #     print("Third point is not joining the line formed by first two points.")

    if p3[0]>=p1[0]:
        if p3[0]>p2[0]:
            print("Right Side")

        elif p3[0]==p2[0]:
            print("Neither")

        else:
            print("Left side")

    else:
        print("left side")

    return 0

strArray1 = [(0, -3), (-2, 0), (0, 0)]
strArray2 = [(0, 0), (0, 5), (0, 2)]

print(line_check(strArray1))
print(line_check(strArray2))

# p1 = (3.0, 5.0)
# p2 = (6.0, 10.0)
# slope = (p2[1] - p1[1])/(p2[0]-p1[0])
# print("Slope is", slope)
# c = p1[1]-slope*p1[0]
# print("Intercept is", c)
# # y = slope*x+c
# print("y =" , slope , "x +" , c)
