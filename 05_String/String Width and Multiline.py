#Width and Multiline

#Data

data_nama = 'Boruto Uzumaki'
data_umur = 17
data_justsu = 'Uzuhiko'

data_string = "Nama : " + data_nama + ",Umur : " + str(data_umur) + ",Jutsu : " + data_justsu
print(" Normal ".center(20, '='))
print(data_string)

data_nama = 'Boruto Uzumaki'
data_umur = 17
data_justsu = 'Uzuhiko'

data_string = f"""
Nama : {data_nama},
Umur : {data_umur},
Jutsu : {data_justsu}
"""
print()
print(" String Multiline ".center(30, '='))
print(data_string)
