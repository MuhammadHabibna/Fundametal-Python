# 1. Cara membuat String

# print("Sekarang Hari Kamis")
# print("Sekarang Hari jum'at")

# # 2. Menggunakna tanda \

#     #membuat tanda '  menjadi string
# print("======= Menggunakan Tanda \ ==========")
# print('mari sholat jum\'at')
# print('g\'dayy isn\'t it ?')

#     #backlash
# print("======= Backlash ==========")
# print("C:\\User\\Habib")

#     #tab
# print("======= tab ==========")
# print("Boruto\tKawaki, Jauhan")

#     #backspace
# print("======= Backspace ==========")
# print("Boruto \bSarada, Deketan")

#     #newline
# print("======= NewLine (Enter) ==========")
# print("Sekarang Hari Kamis\nbesok hari jumat") # LF -> Line Feed (Macos,unix ,linux)
# print("Baris Pertama.\rBaris Kedua.") #CR -> Carriage Return (Commorde, acorn, lisp)
# print("Aku suka bebek\r\nKamu suka Ayam") #CRLF -> Carriage return line feed (Windows)

# 3. String Literal atau raw

#Warning
print("==== Salah Path ====")
print('D:\new Folder') #SALAH PATH
print("====================")

#Menggunakan Raw String
print(r'D:\new Folder') 

#Multiline Literal String
print("""
Nama : Muhammad Habib
Kelas : 24F
Instansi : Unesa
""")

#Multiline Literal String dan Raw

print(r"""
Nama : Muhammad Habib
Kelas : 24F
Instansi : Unesa
Website : https:\\vaeragamestore.id
""")