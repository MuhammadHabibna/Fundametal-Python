## Nested List / List Bersarang

peserta1 = ['Luffy', 18, 'Cowo']
peserta2 = ['Sabo', 20, 'Cowo']
peserta3 = ['Ace', 24, 'Cowo']

list_peserta = [peserta1,peserta2,peserta3]

print(f"Peserta : {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]} ")
    print(f"Umur\t: {peserta[1]} ")
    print(f"Gender\t: {peserta[2]} \n")

    # Matriks(without nested list comprehension)
# matrix = []

# for i in range(5):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(j)
# print(matrix)

#     #Matriks(With nested list comprehension)

# matrix = [[j for j in range(5)] for i in range(5)]
# print(matrix)