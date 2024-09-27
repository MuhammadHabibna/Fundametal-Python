#Latihan logika dan komparasi


# InputUser = float(input("Masukkan Angka : "))

"""
jika suatu bilangan kurang dari 3 dan lebih dari 10 maka True
++++++++3------------10+++++++++++ 
"""

# output = (InputUser < 3 or InputUser > 10)
# print(output)

#------------3++++++++++++10------------- (Irisan)

# output2 = (3 < InputUser < 10)
# print(output2)

'''
Ketika User Input Bilangan antara 0 dan 5 & 8 dan 11 
maka outputnya True 
Buatkan Operasinya !
----------- 0 +++++++ 5 -------- 8 ++++++++ 11 ---------
'''


# inputUser = float(input("Masukkan Angka : "))

# output = 0 < inputUser < 5 or 8 < inputUser < 11
# print(output)

'''
Ketika User Input Bilangan kurang dari 0 & antara 5 dan 8 
& lebih dari 11
maka outputnya True
+++++++++ 0 --------- 5 ++++++++ 8 --------- 11 +++++++++
Buatkan operasinya !
'''


inputUser = float(input("Masukkan Angka : "))

output = not(0 < inputUser < 5 or 8 < inputUser < 11)
print(output)