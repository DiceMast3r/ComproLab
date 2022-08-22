def triangleChecker(a, b, c):
    # put code below
    a = int(a)
    b = int(b)
    c = int(c)
    side = [a, b, c]
    if sum(side[0:2]) == 0:
        print("Side of triangle must not be zero.")
    else:
        neg_count = 0
        for i in side:
            if int(i) < 0:
                neg_count += 1
        if neg_count > 0:
            print("INPUTs cannot be negative.")
        else:
            side.sort()
            zero_count = 0
            for i in side:
                if int(i) == 0:
                    zero_count += 1
            if zero_count > 0:
                print("Side of triangle must not be zero.")
                exit()
            if side[2] > side[0] + side[1]:
                print("==> NOT VALID sides")
            elif side[2] == side[0] == side[1]:
                print("==> Equilateral Triangle")
            elif side[2] == side[0] or side[2] == side[1]:
                print("==> Isosceles Triangle.")
            elif (side[2]**2 == side[0]**2 + side[1]**2):
                print("==> Right Triangle")
            else:
                print("==> Triangle.")


print(" *** Triangle Checker ***")
a, b, c = input("Enter side1 side2 side3 : ").split()
triangleChecker(a, b, c)
