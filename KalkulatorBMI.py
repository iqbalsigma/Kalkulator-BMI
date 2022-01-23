#Kalkulator BMI
#Created by Iqbal Sigma
print("====KALKULATOR BMI====")
TB=float(input("Masukkan tinggi badan dalam cm: "))
BB=float(input("Masukkan berat badan dalam kg: "))
TB = TB/100
BMI=BB/(TB*TB)
print("Angka BMI : ",BMI)
if(BMI>0):
	if(BMI<=18.5):
		print("Anda kekurangan berat badan")
	elif(BMI<=24.9):
		print("Anda normal (ideal)")
	elif(BMI<=29.9):
		print("Anda kelebihan berat badan")
	elif(BMI>=30):
		print("Anda kegemukan (obesitas)")
else:("Masukkan data yang valid")
