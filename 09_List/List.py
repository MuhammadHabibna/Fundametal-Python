## ----- LIST ------

'''
List merupakan tipe data yang digunakan untuk menyimpan
kumpulan item (data) dalam satu variabel
'''

# #  Kumpulan data Interger
# data_int = [1,3,5,6,7,8]
# print(data_int)

# # Kumpulan data float
# data_float = [1.5, 3.24, 51.5, 98.3]
# print(data_float)

# # Kumpulan data String
# data_str = ['Luffy', 'Zoro', 'Sanji']
# print(data_str)

# #Kumpulan data boolean
# data_bool = [True, False, True, False]
# print(data_bool)

# Kumpulan data Campuran
# data_campur = [10, 'Luffy', 15.24, True]
# print(data_campur)

# ## Cara Alternatif Membuat loop

# data_range = range(0, 10, 2) #start, stop, step(jarak)
# print(data_range)
# data_list = list(data_range)
# print(data_list)

# ## List Comprehession

# squared = [i**2 for i in range(0, 10)]
# print(squared)

# # Dengan kondisi if

# squared_genap = [i**2 for i in range(0,10) if i%2 == 0]
# print(squared_genap)

# Dengan kondisi if else

squared_or_cubed = [i**2 if i%2 == 0 else i**3 for i in range(0,10)]
#pangkat 2 jika genap, pangkat 3 jika ganjil
print(squared_or_cubed)
