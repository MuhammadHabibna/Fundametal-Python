# ## Manipulasi List

# # index    0(-4)    1(-3)   2(-2)   3(-1)
# data = ['luffy', 'zoro', 'sanji', 'nami']

# #data pertama dari kiri [0]
# data_kiri = data[0]
# print(data_kiri)

# #data pertama dari kanan [-1]
# data_kanan = data[-1]
# print(data_kanan)

# # Mengambil info jumlah data dalam list
# data = ['luffy', 'zoro', 'sanji', 'nami']
# panjang_data = len(data)
# print(f"panjang data : {panjang_data}")

# # Menambahkan data pada list sesuai
# data = ['luffy', 'zoro', 'sanji', 'nami']
# print(f"data sebelum ditambah : {data}")

# data.insert(1, 'Brook')
# print(f"data setelah ditambah : {data}")

# #Menambahkan data diakhir List
# data = ['luffy', 'zoro', 'sanji', 'nami']
# data.append('Robin')
# print(f"ditambah data lagi : {data}")

# ##  Menambahkan data dengan sebuah data
# data = ['luffy', 'zoro', 'sanji', 'nami']
# data_baru = ['franky','chopper','ussop']
# data.extend(data_baru)
# print(f"Data sudah di extend : {data}")

## Update Data
# Ubah data ke-3 menjadi ussop
# data = ['luffy', 'zoro', 'sanji', 'nami']
# data[3] = 'Usoop'
# print(f"Data setelah Update : {data}")

## Remove Data
data = ['luffy', 'zoro', 'sanji', 'nami']
data.remove("luffy") #penulisan huruf harus sesuai
print(f"Data baru setelah ada yang dihapus : {data}")

#remove data paling terakhir
data = ['luffy', 'zoro', 'sanji', 'nami']
data.pop()
print(f"Data terakhir dihapus : {data}")
