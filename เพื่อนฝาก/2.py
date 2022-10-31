'''
 * กลุ่มที่  : 22010001
 * 65010180 ชนิกานต์ กล่ำเหว่า
 * chapter : 4	item : 4	ครั้งที่ : 0011
 * Assigned : Tuesday 23rd of August 2022 10:50:08 PM --> Submission : Saturday 27th of August 2022 11:21:45 PM	
 * Elapsed time : 5791 minutes.
 * filename : ch4_4.py
'''
def key_int_float(x):
    fraction = x % 1
    if fraction == 0.0 or fraction == -0.0:
        x = int(x)
        return x
    else:
        ans = "{:.1f}".format(x)
        return ans

def xIntercept(m,c):
    try:
        c = float(c); m = float(m)
        x = -c/m # m=-1 c=1; x = 1.0
        ans = key_int_float(x)
        return ans
    except ZeroDivisionError:
        ans = "Not Available"
        return ans

def yIntercept(m,c):
    c = int(c)
    y = c
    return y

print(" *** XY Intercept y = mx + c ***")
m,c = input("Enter m c : ").split()
print ("x-intercept =", xIntercept(m,c))
print ("y-intercept =", yIntercept(m,c))