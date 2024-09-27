print("Selamat Datang".center(50, "="))
print("Kalkulator Sederhana".center(50, "="))

a = int(input("Bilangan 1 : "))
operator = input("Operator (+  - * /) : ")
b = int(input("Bilangan 2 : "))


if operator == "+":
    hasil = a + b
    print(f"Hasil dari {a} {operator} {b} adalah {hasil}")
elif operator == "-":
    hasil = a - b
    print(f"Hasil dari {a} {operator} {b} adalah {hasil}")
elif operator == "*":
    hasil = a * b
    print(f"Hasil dari {a} {operator} {b} adalah {hasil}")
elif operator == "/":
    hasil = a / b
    print(f"Hasil dari {a} {operator} {b} adalah {hasil}")
else:
    print("Operator Tidak Sesuai!!")