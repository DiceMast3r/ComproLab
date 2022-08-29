'''
 * กลุ่มที่  : 22010001
 * 65010386 ธงชัย พันธุ์ไพศาล
 * chapter : 3	item : 1	ครั้งที่ : 0001
 * Assigned : Monday 15th of August 2022 10:27:12 AM --> Submission : Monday 15th of August 2022 10:34:28 AM	
 * Elapsed time : 7 minutes.
 * filename : ch3_1.py
'''
print(" *** Number Manipulation ***")
num = int(input("Enter a whole number : "))
if num % 2 == 0:
    print("%d is even." %num)
else:
    print("%d is odd." %num)
print("absolute value of %d ==> %d"%(num, abs(num)))