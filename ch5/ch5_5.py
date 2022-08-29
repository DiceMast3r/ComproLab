print(" *** even integer summation from 1 to n ***")
n = int(input("Enter an integer(n) : "))
fac = n
i = 1
sum = ""
sum_i = 1
while i < n:
    if n % 2 == 0:
        if n == 2:
            break
        sum = "+" + str(n) + sum
        sum_i = n + sum_i
        n -= 2
    else:
        n -= 1
sum = str(n) + sum
sum_i = 1 + sum_i
print("Summation => {0} = {1}".format(sum ,sum_i))