#Operasi dan manipulasi String

# # 1. Menyambung String (concatenate)
# nama_depan = "Monkey"
# marga = "D"
# nama_akhir = "Luffy"
# nama_panjang = nama_depan + ' ' + marga+'. ' + nama_akhir
# print(nama_panjang)
# print("Aku adalah", nama_panjang, "Orang yang akan menjadi raja bajak laut.")


# # 2. Menghitung Panjang String
# panjang = len(nama_panjang) #spasi masuk hitungan
# print("nama_panjang memiliki ",panjang, " huruf")

# # 3. Operator untuk string 
# #Mengecheck apakah ada komponen char or string dalam string

# print('nama panjang : ',nama_panjang)
# check = 'o'
# status = check in nama_panjang
# print("Apakah ada huruf", check, "di nama panjang : ", str(status))

# check_nama = 'luffy'
# status_nama = check_nama in nama_panjang
# print("Apakah ada nama", check_nama,"di nama panjang : ", status_nama)


# # 4. Mengulang String
# print("ha"*15)
# print(13*"wk")

# # 5. Indexing

# print("Index ke-0 :", nama_panjang[0])
# print("Index ke-5 :", nama_panjang[5])
# print("Index ke-(-1) :", nama_panjang[-1])
# print("Index ke-(0 sampai 5) :", nama_panjang[0:6])
# print("Index ke-(0,2,4,6,8,10) :", nama_panjang[0:10:2])

# # 6. Item Paling Kecil/Besar (ASCII code)

# ascii_code = ord("m") #check string, ascii ke berapa ?
# print("ASCII code untuk huruf m : ", str(ascii_code))

# data = chr(ascii_code) #check ascii, string apa ?
# print("ASCII ke", ascii_code,"adalah huruf : ", data)

# # 7. Operator dalam bentuk method

# data = "ini inik bingit lihh.."
# jumlah = data.count("i")
# print("jumlah huruf i pada", data ,"adalah : ", jumlah)

# # 8. Mengubah Semua ke UpperCase

# print("====== MERUBAH KE HURUF KAPITAL ======")
# salam = "yO!, brOOooKuuu"
# print("Normal : ", salam)

# salam = salam.upper()
# print("Upper : ", salam)

# # 9. Mengubah semua ke LowerCase

# print("====== MERUBAH KE HURUF KECIL ======")
# sapa = "SeLAMaT DaTAnG bRO KU!"
# print('Normal :', sapa)

# sapa = sapa.lower()
# print('Lower : ', sapa)

# # 10. Pengecheckan dengan isX Method

#     #Check apakah lowerCase/UpperCase
# print("======= Apakah Lower ? =======")
# tanya = "halo, asal kamu darimana?"
# apakah_lower = tanya.islower()
# print(tanya, 'is lower = ', apakah_lower)

# print("======= Apakah Upper ? =======")
# nama = "MONKEY D. LUFFY"
# apakah_upper = nama.isupper()
# print(nama, 'is upper = ', apakah_upper)

'''
Contoh Lain :
isalpha() <-- untuk mengecheck apakah semuanya huruf (string) ?
isalnum() <-- Huruf dan Angka
isdecimal() <-- apakah semuanaya angka(int) ?
isspace() <-- spasi, tab, newline
istitle() <-- Apakah semua kata diawali huruf Kapital ?
'''

#Penggabungan data terpisah join(), split()

# list = ['Mess', 'Hilgers', 'Bergabung', 'Indonesia']
# print("Normal :", list)

# kalimat = ' '.join(list)
# print("Kalimat :", kalimat)

# kalimat_koma = ','.join(list)
# print("Kalimat dengan koma :", kalimat_koma)

# #Penggabungan data terpisah join(), split()

# kalimat = 'Indonesia,Australia,Japan,Arab Saudi,Bahrain,China'
# print(kalimat.split(','))

# # Alokasi Character rjust(), ljust(), center()

# right = "right".rjust(10, ">") #panjang, simbol
# print("'"+right+"'")

# left = "left".ljust(10, "<") 
# print("'"+left+"'")

# center = "center".center(20, "=") 
# print("'"+center+"'")

# Kebalikan --> strip()

# center = "center".center(20, "=")  #======center======
# center_strip = center.strip('=') #menghilangkan tanda "="
# print(center_strip)
 