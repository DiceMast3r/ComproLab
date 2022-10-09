'''
 * กลุ่มที่  : 22010001
 * 65010386 ธงชัย พันธุ์ไพศาล
 * chapter : 2	item : 3	ครั้งที่ : 0008
 * Assigned : Monday 8th of August 2022 10:55:48 AM --> Submission : Monday 8th of August 2022 11:53:41 AM	
 * Elapsed time : 57 minutes.
 * filename : ch2_3.py
'''
print(" *** Finding circle area *** ")
radius = input("Enter radius : ")
radius = float(radius)
pi = 3.1415926
circleArea = pi * radius * radius
print("Circle area =", circleArea)
print("Circle area = %.2f" %circleArea) # แสดงผลทศนิยม 2 ตำแหน่ง
print("whole number =>",int(circleArea)) # แสดงผลเฉพาะส่วนที่เป็นจำนวนเต็ม
