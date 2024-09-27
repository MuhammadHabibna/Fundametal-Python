array = [-64, -75, -51, -3, 2, 6, 12, 53, -80, 34]
lenght = len(array)

def selectionsort():
    for i in range(0, lenght):
        min = i
        for j in range(i+1, lenght):
            if array[j] < array [min]:
                min = j
        temp = array[min]
        array[min] = array[i]
        array[i] = temp
    print(array)

# selectionsort()


# array = [-64, -75, -51, -3, 2, 6, 12, 53, -60, 34]
def sortirtolower():
    for i in range(0, lenght):
        max = i
        for j in range(i+1, lenght):
            if array[max] < array[j]: #j=1 masih sama | j=2 --> -51,-75,-64 | j = 3 --> -3, -75, -64, -51,.. | j = 4 --> 2, -75, -64, -51, .. | hingga 53
                max = j
        temp = array[max]
        array[max] = array[i]
        array[i] = temp
    print(array)




# selectionsort()
sortirtolower()

# array = [16, 48, 89, 14, 62, 45, 81, 32, 43, 60]
# lenght = len(array)

# nilai_maks = 0

# for i in range(0, lenght):
#     if array[i] > nilai_maks:
#         nilai_maks = array[i]


# maks_while = array[0]
# i = 0

# while i < lenght:
#     if array[i] > maks_while:
#         maks_while = array[i]
#     i += 1

# print(f"Mencari nilai maks, Menggunakan For : {nilai_maks}")
# print(f"Mencari nilai maks, Menggunakan While : {maks_while}")