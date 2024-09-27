#Operasi Logika dan boolean

#not, or, and, xor

#Not 
# print('===== NOT =====')
# a = True
# b = not a
# print('Nilai dari a : ', a)
# print('Nilai dari b (not a) : ', b)

# # OR
# print('===== OR =====')
# a = True 
# b = False
# c = a or b
# print(a,'OR',b, ':', c)
# #Bernilai benar jika salah satu/kedua input 'benar'

# # AND
# print('===== AND =====')
# a = True
# b = False
# c = True and False
# print(a,'AND',b, ':', c)
# #Bernilai benar jika kedua input 'benar'

# # XOR 
# print('===== XOR =====')
# a = False
# b = True
# c = a ^ b
# print(a,'XOR',b, ':', c)
# #Bernilai benar jika kedua input berbeda

#STUDY CASE

# ''''
# Latar Belakang:
# Sebuah toko elektronik online ingin mengembangkan sistem rekomendasi untuk membantu pelanggannya memilih 
# perangkat elektronik (laptop, tablet, atau smartphone). Sistem ini akan merekomendasikan produk yang sesuai 
# dengan kebutuhan pelanggan berdasarkan beberapa kriteria seperti harga, kapasitas penyimpanan, dan daya tahan baterai.

# Deskripsi Masalah:
# Kriteria:

# Harga:
# Murah: Di bawah 5 juta
# Sedang: Antara 5 juta hingga 10 juta
# Mahal: Di atas 10 juta

# Kapasitas Penyimpanan:
# Kecil: Di bawah 128 GB
# Sedang: Antara 128 GB hingga 512 GB
# Besar: Di atas 512 GB

# Daya Tahan Baterai:
# Rendah: Di bawah 8 jam
# Sedang: Antara 8 hingga 12 jam
# Tinggi: Di atas 12 jam
# Aturan Rekomendasi:

# Jika harga murah dan kapasitas penyimpanan kecil, rekomendasikan "Tablet".
# Jika harga sedang atau murah dan daya tahan baterai tinggi, rekomendasikan "Smartphone".
# Jika harga mahal dan kapasitas penyimpanan besar, rekomendasikan "Laptop".
# Jika tidak memenuhi semua kriteria di atas, rekomendasikan "Periksa lebih lanjut".
# Tugas:
# Buatlah fungsi Python menggunakan operasi logika Boolean untuk mengimplementasikan aturan rekomendasi tersebut.
# Fungsi tersebut harus menerima input dari pengguna mengenai harga, kapasitas penyimpanan, dan daya tahan baterai,
# kemudian memberikan rekomendasi produk yang sesuai.
# '''

harga = int(input("harga : "))
penyimpanan = int(input("Kapasitas Penyimpanan (gb) = "))
baterai = int(input("Daya Tahan Baterai (jam)= "))

print('\n')

low_harga = 5000000
high_harga = 10000000
low_penyimpanan = 128
high_penyimpanan = 512
low_baterai = 8
high_baterai = 12

if(harga < low_harga and penyimpanan < low_penyimpanan):
    output = "Tablet"
    print("Rekomendasi = ", output)
elif(harga < high_harga and baterai > high_baterai):
    output = "Smartphone"
    print("Rekomendasi = ", output)
elif(harga > high_harga and penyimpanan > high_penyimpanan):
    output = "Laptop"
    print("Rekomendasi = ", output)
else:
    print("Periksa Lebih Lanjut")

