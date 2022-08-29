def adder(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        sum = num1 + num2
        return sum
    except ValueError:
        num1 = float(num1)
        num2 = float(num2)
        sum = num1 + num2
        return sum

print(" **** Adder Function ***")
num1, num2 = input('Enter 2 numbers: ').split()
result = adder(num1, num2)  
# f-string(เอฟสตริง) คือการสร้าง string จากตัวแปร
# ใช้ได้ตั้งแต่ version 3.6 ขึ้นไป

# โดยจะนำค่าของตัวแปร มาแทนที่ วงเล็บปีกกา (curly brace)
fstring = f"{num1} + {num2} = {result}"
print(fstring)  