print("Sum of 1 to n!")
n = int(input("Enter an n: "))
n2 = n
i = 1
sum = 0
sum_s = ""
while i < n:
    sum_s = "+" + str(n) + sum_s
    sum += n
    n -= 1
sum_s = str(n) + sum_s
sum += n
print("Sum of 1 to {0} is {1}: {2}".format(n2, sum_s, sum))