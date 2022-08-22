def slope(a,b,c):
    # put code below
    a = float(a)
    b = float(b)
    c = float(c)
    try:
        m = -a / b
    except ZeroDivisionError:
        m = "Not Available"
        return m
    if m % 1 == 0 or m % 1 == -0:
        m = int(m)
    return m

def xIntercept(a,b,c):        
    # put code below
    a = float(a)
    b = float(b)
    c = float(c)
    try:
        x_i = -c / a
    except ZeroDivisionError:
        x_i = "Not Available"
        return x_i
    if x_i % 1 == 0 or x_i % 1 == -0:
        x_i = int(x_i)
    return x_i
    
def yIntercept(a,b,c):  
    # put code below
    a = float(a)
    b = float(b)
    c = float(c)
    try:
        y_i = -c / b
    except ZeroDivisionError:
        y_i = "Not Available"
        return y_i
    if y_i % 1 == 0 or y_i % 1 == -0:
        y_i = int(y_i)
    return y_i
    
print(" *** XY  Intercept ***\n -- ax + by + c = 0 --")
a,b,c = input("Enter a b c : ").split()
print("Slope = {0}".format(slope(a,b,c)))
print("x-intercept => {0}".format(xIntercept(a,b,c)))
print("y-intercept => {0}".format(yIntercept(a,b,c)))
