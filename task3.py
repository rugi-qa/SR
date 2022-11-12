n = int(input())  # Задаем размер матрицы
x = int(input())  # Задаем x
total = 0  # Задаем сумму
for i in range(1, n + 1):  # Цикл по строкам
    for j in range(1, n + 1):  # Цикл по столбцам
        elem = x ** abs((j - i)) 
        if 1 < i < n and 1 < j < n:
            elem = 0
        print(elem, end = " ")
    print("")
