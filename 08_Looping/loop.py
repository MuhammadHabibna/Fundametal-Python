# a = 1
# b = 100
# jumlah_ganjil = 0

# for x in range(a,b):
#     if x%2==1:
#         jumlah_ganjil += x
# print("========= Jumlah Bilangan Ganjil ==========")
# print(f"Jumlah Bilangan Ganjil antara {a} dan {b} adalah {jumlah_ganjil}")

# #Tabel Perkalian

# hasil = 0
# print("======= Tabel Perkalian =======")
# for x in range(1,11):
#     print("\n")
#     for y in range(1,11):
#         hasil = x*y
#         print(f"{x} x {y} = {hasil}")


# # Deret Fibonacci

# n = 10
# num1, num2 = 0, 1

# fibonacci = [num1, num2]

# for i in range (2, n):
#     next_num = num1 + num2
#     fibonacci.append(next_num)
#     num1, num2 = num2, next_num

# print(f"Fibonacci : {fibonacci}")

#jumlah bil. prima

def is_prima(x):
    for i in range(2, x):
        if x % i == 0:
            return False #bukan prima
    return True

jumlah_prima = 0
prima = []

for i in range(1,50 + 1):
    if is_prima(i):
        jumlah_prima += i
        prima.append(i)

print(f"Bilangan prima {prima}")
print(f"Jumlah bilangan prima antara 1 sampai 50 adalah {jumlah_prima}")



