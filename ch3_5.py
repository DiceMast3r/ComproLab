print(" *** Transform second ***")
second = 0
try:
    second = input("Enter seconds : ")
    second = int(second)
    w = (str(second // 604800) + " weeks ") * ((second // 604800) > 0) #str * bool
    d = (str(((second % 604800) // 86400)) + " days ") * (((second % 604800) // 86400) > 0)
    h = (str(((second % 86400) // 3600)) + " hours ") * (((second % 86400) // 3600) > 0)
    m = (str((second % 3600) // 60) + " minutes ") * (((second % 3600) // 60) > 0)
    s = (str(second % 60) + " seconds ") * ((second % 60) > 0)
    print(second, "seconds ==>" +f' {w}{d}{h}{m}{s}')
except ValueError:
    print("! ! ! please enter in whole number --> {0}".format(second))
print(" --- program end --- ")