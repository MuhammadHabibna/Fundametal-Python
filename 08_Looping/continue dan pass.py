#Continue and Pass

# pass --> berfungsi sebagai dummy( Tidak akan di eksekusi )

angka = 0

while angka < 5:
    angka += 1
    
    if angka == 3:
        pass # Tidak melakukan apa-apa ketika angka sama dengan 3
    else: 
        print(f"HALO HALO {angka}")

#continue 

# angka = 0

# while angka < 5:
#     angka += 1

#     print(f"Angka sekarang adalah {angka}") #Aksi 1

#     if angka == 3:
#         print(f"I Love 3")
#         continue #akan membuat loop loncat ke step selanjutnya
#                 #mengabaikan aksi selanjutnya.

#     print("Halo") #Aksi 2

#break 

# angka = 0

# while angka < 5:
#     angka += 1
#     print(f"Sekarang Angka {angka}")

#     if angka == 4:
#         print(f"Angka Mencapai 4")
#         break
    
#     print(f"Good!")

# print(f"Program Selesai")