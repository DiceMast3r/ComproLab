file = open("ch8\data1.txt", "r")
print("File name: ", file.name)
print("Original data:")
for line in open("ch8\data1.txt", "r"):
    print(line, end="")


data_in = input("\nEnter data to write to file: ")
f = open("ch8\data1.txt", "a")
f.write('\n' + data_in)
f.close()
print("Data written to file.")
print("New data:")
for line in open("ch8\data1.txt", "r"):
    print(line, end="")