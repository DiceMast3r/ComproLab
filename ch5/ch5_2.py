print(" *** integer summation from 1 to n ***")
n = int(input("Enter an integer(n) : "))
i = 1
sum = ""
sum_i = 0
while i < n:
    sum = "+" + str(n) + sum
    sum_i = n + sum_i
    n -= 1
sum = str(n) + sum
sum_i = n + sum_i
print("Summation => {0} = {1}".format(sum,sum_i))