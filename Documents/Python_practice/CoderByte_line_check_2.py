def point(p1, p2, p3):
    s = 1
    try:
        m = float((p2[1] - p1[1])/(p2[0]-p1[0]))
        # print("Slope of the line is:", m)
    except(ZeroDivisionError):
        # print("Line is perpendicular to x-axis")
        s = 0

    if s !=0:
        print("Slope of the line is:", m)
        c = p1[1]-m*p1[0]
        print("The equation of the line is: y = ", m, "x +", c)

        if p2[0]>=p1[0]:
            if (m*p3[0] - p3[1] + c) > 0:
                print("Right Side")

            elif (m*p3[0] - p3[1] + c) < 0:
                print("Left side")

            else:
                print("Neither")

        else:
            if (m*p3[0] - p3[1] + c) > 0:
                print("Left Side")

            elif (m*p3[0] - p3[1] + c) < 0:
                print("Right side")

            else:
                print("Neither")

    else:
        print("Line is perpendicular to x-axis")
        k = p1[0]
        print("The equation of the line is: x = ", k)

        if p2[0]>=p1[0]:
            if (p3[0] + k) > 0:
                print("Right Side")

            elif (p3[0] + k) < 0:
                print("Left side")

            else:
                print("Neither")

        else:
            if (p3[0] + k) > 0:
                print("Left Side")

            elif (p3[0] + k) < 0:
                print("Right side")

            else:
                print("Neither")


def line_check(strArray):
    print("Array is:", strArray)

    p1 = strArray[0]
    p2 = strArray[1]
    p3 = strArray[2]

    point(p1, p2, p3)

strArray1 = [(0, -3), (-2, 0), (0, 0)]
strArray2 = [(-2, 0), (0, -3), (0, 0)]
strArray3 = [(0, 0), (0, 5), (0, 2)]

print(line_check(strArray1))
print(line_check(strArray2))
print(line_check(strArray3))
