# sisi = 10

# for i in range(sisi):
#     print("*" * i)

# i = 0
# while i < sisi:
#     print("*" * i)
#     i += 1

#Segitiga Sama Kaki

# tinggi = 10

# for i in range(1, tinggi):
#         print("\n")
#         print(" " * (tinggi - i) + "*" * (2*i - 1))

print("AWAL WHILE")
sisi = 7
spasi = int(sisi/2)
count = 1

while True:
    if(count%2): #0 false, #1 true (JIKA Ganjil Program ini berjalan)
          #Print jika ganjil
          print(" " * spasi + "*" * count)
          spasi -= 1
          count += 1
    else:
          count += 1 #
          continue
    
    if count > sisi:
          break
print("Akhir While")