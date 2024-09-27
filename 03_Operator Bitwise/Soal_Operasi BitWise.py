'''
Kontrol Perangkat Elektronik

Soal: Anda bekerja sebagai pengembang perangkat lunak untuk sistem rumah pintar.
Dalam sistem ini, perangkat elektronik (lampu, kipas angin, dan pemanas) dikendalikan 
oleh satu variabel status yang terdiri dari 3 bit. Bit pertama mewakili status lampu, 
bit kedua untuk kipas angin, dan bit ketiga untuk pemanas. Jika bit bernilai 1, perangkat
tersebut menyala, dan jika 0, perangkat tersebut mati.

Tugas:

1). Tentukan status awal dari perangkat jika 'status = 5'. Gunakan operator bitwise untuk menampilkan kondisi setiap perangkat.
2). Tuliskan kode Python untuk mematikan lampu tanpa mengubah status perangkat lainnya.
3). Tuliskan kode Python untuk menyalakan kipas angin tanpa mengubah status perangkat lainnya.
4). Jika perangkat dalam kondisi 'status = 7', tuliskan kode Python untuk mematikan semua perangkat secara bersamaan.
'''


status = 5 #0b101 
#lampu Menyala, kipas Mati, pemanas Menyala

lampu = status & 0b001
kipas = (status & 0b010) >> 1
pemanas = (status & 0b100) >> 2

print("======= KONDISI SEKARANG : =======")
print(bin(status))
print(f"Lampu: {'Menyala' if lampu == 1 else 'Mati'}")
print(f"Kipas Angin: {'Menyala' if kipas == 1 else 'Mati'}")
print(f"Pemanas: {'Menyala' if pemanas == 1 else 'Mati'}")

print()
print("=======MATIKAN LAMPU=======")
print()

status = status & 0b110
print(bin(status)) #0b100

print()
print("=======NYALAKAN KIPAS ANGIN=======")
print()

status = status | 0b110
print(bin(status)) #110

print()
print("======= MATIKAN SEMUA JIKA STATUS = 7 (0b111)=======")
print()

if status == 7:
    status = status & 0b000
    print(bin(status))
else:
    print("Eror!, Perangkat tidak bernilai 7 atau 0b111")


#STUDY CASE 2

# String yang akan dienkripsi
plaintext = "HELLO"
# Kunci untuk enkripsi
k = 5

# Mengenkripsi setiap karakter dalam string
encrypted_text = ''.join([chr(ord(char) ^ k) for char in plaintext])
# if 10 ^ 5 = 15, maka 15 ^ 5 = 10
descrypted_text = ''.join([chr(ord(char) ^ k) for char in encrypted_text])
# ord = String to ASCII, chr ASCII to string
print("descrypted_text : ", descrypted_text)

'''
Sifat Simetris: XOR memiliki sifat yang memungkinkan enkripsi dan dekripsi dilakukan dengan operasi yang sama. 
Ini sangat berguna dalam enkripsi sederhana karena satu operasi dapat membalikkan hasil enkripsi.

Kesederhanaan: Operasi XOR sangat sederhana dan cepat dijalankan oleh komputer, 
sehingga ideal untuk aplikasi di mana kecepatan adalah faktor penting
'''
