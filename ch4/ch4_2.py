def quadraticChecker(a :float, b :float, c :float):
    # Enter your code
    x = (b**2)-(4*a*c)
    return x

print(" *** Quadratic Checker *** ")
print("     ax^2 + bx + c = 0     ")
a,b,c = input("Enter a b c : ").split()
# Enter your code below
try:
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        print("a must NOT be zero !!!")
        exit()
except ValueError:
    print("Please enter VALID a, b and c !!!")
    exit()
    

checker = quadraticChecker(a,b,c) # invoke function
if checker == 0:
    print("There is only ONE solution.")
elif checker < 0:
    print("There is NO VALID solution.")
else:
    print("There are TWO solutions.")
