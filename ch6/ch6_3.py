n = int(input("How big is the triangle : "))
if n < 0:
    print("Input Error")
elif n == 0:
    exit()
else:
    for i in range(n):
        print("*" * (i+1))

