n=int(input('Введите n - размерность матрицы nxn:'))
w=input('Параметр 1:')
q=input('Параметр 2:')
elem = 0
total_1, total_2, total_3 = 0, 0, 0
for i in range(0, n):
    for j in range(1, n + 1):
        elem = int(w)
        if i + 1 < j < n - i and i < n - i or n - i < j < i + 1 and i > n - i:
            elem = int(q)
        print(elem, end = ' ')
        if j == n - 2:
            total_3 += elem
        if j == n - 1:
            total_2 += elem
        if j == n:
            total_1 += elem
    print("")
print("Сумма 3-его с конца столбца: ", total_3)
print("Сумма 2-ого с конца столбца: ", total_2)
print("Сумма 1-ого с конца столбца: ", total_1)
print("Сумма трех последних столбцов: ", total_1 + total_2 + total_3)
