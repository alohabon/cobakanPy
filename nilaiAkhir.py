
#pengimputan data
nama = input("Nama : ")
kelas = input("Kelas : ")
nim = input("NIM : ")
tugas1 = input("Nilai Tugas 1 : ")
uts = input("Nilai UTS : ")
tugas2 = input("Nilai Tugas 2 : ")
uas = input("Nilai UAS : ")

#penghitungan nilai bobot 
tugas1 = int(tugas1)*25/100;
tugas2 = int(tugas2)*30/100;
uts = int(uts)*25/100;
uas = int(uas)*20/100;
hasil = tugas1+tugas2+uts+uas;

#menampilkan nilai
print ("\nNama          : ", nama)
print ("Kelas         : ", kelas)
print ("NIM           : ", nim)
print ("Nilai Tugas 1 : ", tugas1)
print ("Nilai UTS     : ", uts)
print ("Nilai Tugas 2 : ", tugas2)
print ("Nilai UAS     : ", uas)
print ("Hasil Akhir   : ",float(hasil))

#untuk menentukan nilai akhirnya
if hasil >=80.01 and hasil <=100:
	print ("\nIndeks : A")
elif hasil >=70.01 and hasil <=80:
	print ("\nIndeks : AB")
elif hasil >=65.01 and hasil <=70:
	print ("\n Indeks : B")
elif hasil >=60.01 and hasil <=65:
	print ("\n Indeks : BC")
elif hasil >=50.01 and hasil <=60:
	print ("\n Indeks : C")
elif hasil >=40.01 and hasil <=50:
	print ("\n Indeks : D")
elif hasil >= 0 and hasil <=40:
	print ("\n Indeks : E")




