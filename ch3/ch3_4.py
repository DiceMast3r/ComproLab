'''
 * กลุ่มที่  : 22010001
 * 65010386 ธงชัย พันธุ์ไพศาล
 * chapter : 3	item : 4	ครั้งที่ : 0002
 * Assigned : Monday 15th of August 2022 11:26:36 AM --> Submission : Monday 15th of August 2022 11:36:29 AM	
 * Elapsed time : 9 minutes.
 * filename : ch3_4.py
'''
print(" *** Grade Classification ***")
score = int(input("Enter your score : "))
if score >= 0 and score <= 100:
    if score >= 80:
        print("Grade A")
    elif score >= 75:
        print("Grade B+")
    elif score >= 70:
        print("Grade B")
    elif score >= 65:
        print("Grade C+")
    elif score >= 60:
        print("Grade C")
    elif score >= 55:
        print("Grade D+")
    elif score >= 50:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("{0:.1f} is invalid ! ! !".format(score))