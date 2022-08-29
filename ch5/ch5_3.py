print(" *** Factorial ***")
n = int(input("Enter an integer(n) : "))
fac = n
i = 1
sum = ""
sum_i = 1
while i < n:
    sum = "*" + str(n) + sum
    sum_i = n * sum_i
    n -= 1
sum = str(n) + sum
sum_i = n * sum_i
print("Fac({0}) => {1} = {2}".format(fac ,sum ,sum_i))