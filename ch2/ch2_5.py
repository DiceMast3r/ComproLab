'''
 * กลุ่มที่  : 22010001
 * 65010386 ธงชัย พันธุ์ไพศาล
 * chapter : 2	item : 5	ครั้งที่ : 0001
 * Assigned : Monday 8th of August 2022 11:15:19 AM --> Submission : Monday 8th of August 2022 11:26:40 AM	
 * Elapsed time : 11 minutes.
 * filename : ch2_5.py
'''
print(" *** Number Fun !!! ***")
a,b = input("Enter a b : ").split()
print("a=",a,"\ttype =",type(a))
print("b=",b,"\ttype =",type(b))
adivb = float(a) / float(b)
bdiva = float(b) / float(a)
adivb_2 = float(a) // float(b)
bdiva_2 = float(b) // float(a)
amodb = float(a) % float(b)
bmoda = float(b) % float(a)
print("a/b = %.2f" %adivb) # แสดงผล a/b ทศนิยม 2 ตำแหน่ง
print("b/a = %.3f" %bdiva) # แสดงผล b/a ทศนิยม 3 ตำแหน่ง
print("a/b = %d r %d" %(adivb_2, amodb)) # แสดงผลการหารแบบเหลือเศษของ a และ b
print("b/a = %d r %d" %(bdiva_2, bmoda))# แสดงผลการหารแบบเหลือเศษของ b และ a
