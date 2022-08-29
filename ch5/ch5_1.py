print(" *** digit count ***")
n = int(input("Enter an integer : "))
i = 0
while n != 0:
    n = n // 10
    i += 1
print("Total digits are:  {0}".format(i))