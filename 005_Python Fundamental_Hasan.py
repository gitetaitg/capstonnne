#1

#Jawaban (belum selesai)(sudah diperbaiki)

# x = 4
# y = 3
# z = 2

# w = ((x + y * z )/( x * y))**2
# print(w)

# 2

#Jawaban (belum selesai)

# a = 0.4 * b
# b = 1 * 


#5

#Jawaban

# num = int(input("Masukkan angka berapapun: "))
# num_kuadrat = num ** 2
# print ("Kuadrat dari " + str(num) + " adalah " + str(num_kuadrat))

#4

#Jawaban

# Harga_Apel = 10000
# Harga_Jeruk = 15000
# Harga_Anggur = 20000

# Jumlah_Apel = int(input("Masukkan Jumlah Apel "))
# Jumlah_Jeruk = int(input("Masukkan Jumlah Jeruk "))
# Jumlah_Anggur = int(input("Masukkan Jumlah Anggur "))

# Total_Harga_Apel = Jumlah_Apel*Harga_Apel
# Total_Harga_Jeruk = Jumlah_Jeruk*Harga_Jeruk
# Total_Harga_Anggur = Jumlah_Anggur*Harga_Anggur

# print("Detail Belanja")
# print("Apel: " + str(Jumlah_Apel) + " x " + str(Harga_Apel)  +  ' = ' + str(Total_Harga_Apel))
# print("Jeruk: " + str(Jumlah_Jeruk) + " x " + str(Harga_Jeruk)  +  ' = ' + str(Total_Harga_Jeruk))
# print("Anggur: " + str(Jumlah_Anggur) + " x " + str(Harga_Anggur)  +  ' = ' + str(Total_Harga_Anggur))
# print("Total: " + str(Total_Harga_Apel + Total_Harga_Jeruk + Total_Harga_Anggur))

#7

#Jawaban


# jumlah_total_hari = int(input("Masukkan jumlah hari "))
# jumlah_tahun = jumlah_total_hari//360
# jumlah_bulan = (jumlah_total_hari%360)//30
# jumlah_minggu = (jumlah_total_hari%360%30)//7
# jumlah_sisa_hari = jumlah_total_hari%360%30%7

# print(str(jumlah_tahun) + " tahun " + str(jumlah_bulan) + " bulan " + str(jumlah_minggu) + " minggu " + str(jumlah_sisa_hari) + " hari ")

#8

#Jawaban

# num = int(input("input a number "))
# if num%2 == 0:
#     print("Number " + str(num) + " is even")
# else:
#     print("Number " + str(num) + " is odd")

#9

#Jawaban

# Massa = int(input("Masukkan Massa(kg) " ))
# Tinggi = int(input("Masukkan Tinggi(cm) " ))/100

# IMT = Massa/Tinggi**2

# if IMT < 0:
#     print("NGAWUR KAU ISI DATA YANG BENAR LAH!!!!")
# elif IMT > 0 and IMT < 18.5:
#     print("Indeks Massa Tubuhmu adalah " + str(IMT) + ", BERAT BADAN KURANG!!")
# elif IMT >= 18.5 and IMT < 25:
#     print("Indeks Massa Tubuhmu adalah " + str(IMT) + ", BERAT BADANMU IDEAL!!")
# elif IMT >= 25 and IMT < 30:
#     print("Indeks Massa Tubuhmu adalah " + str(IMT) + ", BERAT BADANMU BERLEBIH!!")
# elif IMT >= 30 and IMT < 40:
#     print("Indeks Massa Tubuhmu adalah " + str(IMT) + ", BERAT BADANMU SANGAT BERLEBIH!!")
# else:
#     print("Indeks Massa Tubuhmu adalah " + str(IMT) + ", OBES BRO!!!!")

#10

#Jawaban (belum selesai)

# Harga_Apel = 10000
# Harga_Jeruk = 15000
# Harga_Anggur = 20000

# Jumlah_Apel = int(input("Masukkan Jumlah Apel "))
# Jumlah_Jeruk = int(input("Masukkan Jumlah Jeruk "))
# Jumlah_Anggur = int(input("Masukkan Jumlah Anggur "))

# Total_Harga_Apel = Jumlah_Apel*Harga_Apel
# Total_Harga_Jeruk = Jumlah_Jeruk*Harga_Jeruk
# Total_Harga_Anggur = Jumlah_Anggur*Harga_Anggur
# Total = Total_Harga_Apel + Total_Harga_Jeruk + Total_Harga_Anggur

# print("Detail Belanja")
# print("Apel: " + str(Jumlah_Apel) + " x " + str(Harga_Apel)  +  ' = ' + str(Total_Harga_Apel))
# print("Jeruk: " + str(Jumlah_Jeruk) + " x " + str(Harga_Jeruk)  +  ' = ' + str(Total_Harga_Jeruk))
# print("Anggur: " + str(Jumlah_Anggur) + " x " + str(Harga_Anggur)  +  ' = ' + str(Total_Harga_Anggur))
# print("Total: " + str(Total))

# Jumlah_Uang = int(input("Masukkan uang anda "))


# if Jumlah_Uang < Total:
#     print("Transaksi dibatalkan\nUangnya kurang sebesar " + str(Total - Jumlah_Uang))
# elif Jumlah_Uang == Total:
#     print("Terima Kasih")
# else:
#     print("Terima kasih\nUang kembali anda: " + str(Jumlah_Uang - Total))

angkaString = input("Masukkan suatu angka ")
digitAngka = len(angkaString)

# print(digitAngka)
sumAngkaPangkat = 0
for i in angkaString:
    angkaPangkat = int(i)**digitAngka
    sumAngkaPangkat += angkaPangkat
print(sumAngkaPangkat)