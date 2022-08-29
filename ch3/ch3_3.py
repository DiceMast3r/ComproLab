print(" *** Data type integer float string ***")
data_in = input("Enter a word : ")
try:
    data_in = int(data_in)
    print("{0} * 2 = {1}".format(data_in, data_in * 2))
except ValueError:
    try:
        data_in = float(data_in)
        print("{0:.3f} / 3 = {1:.3f}".format(data_in, data_in / 3))
    except ValueError:
        print("{0} {1} {2}".format(data_in, data_in, data_in))
