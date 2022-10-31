fibo = []
x, y, z = 0, 1, 0
n = int(input("Enter an n for fibo: "))
for i in range(n):
    fibo.append(x)
    z = x + y
    x = y
    y = z
print(fibo)