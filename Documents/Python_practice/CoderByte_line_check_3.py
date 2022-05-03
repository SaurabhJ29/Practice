def side(p1, p2, p3):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0]*p1[1] - p1[0]*p2[1]
    print("  The equation of the line is: ", a, "x + ", b, "y +", c, "= 0" )

    if (a*p3[0] + b*p3[1] + c) > 0:
        print("\tRight Side")

    elif (a*p3[0] + b*p3[1] + c) < 0:
        print("\tLeft side")

    else:
        print("\tNeither")


    # if p2[1]>=p1[1]:
    #     if (a*p3[0] + b*p3[1] + c) > 0:
    #         print("\nRight Side")

    #     elif (a*p3[0] + b*p3[1] + c) < 0:
    #         print("\nLeft side")

    #     else:
    #         print("\nNeither")

    # else:
    #     if (a*p3[0] + b*p3[1] + c) > 0:
    #         print("\nRight Side")

    #     elif (a*p3[0] + b*p3[1] + c) < 0:
    #         print("\nLeft side")

    #     else:
    #         print("\nNeither")


def line_check(strArray):
    print("\nPoints of the line are:", strArray)

    p1 = strArray[0]
    p2 = strArray[1]
    p3 = strArray[2]

    side(p1, p2, p3)

strArray1 = [(0, -3), (-2, 0), (1, 0)]
strArray2 = [(-2, 0), (0, -3), (1, 0)]
strArray3 = [(0, 0), (0, 5), (0, 2)]

line_check(strArray1)
line_check(strArray2)
line_check(strArray3)

# (0, 0) always changes the things.