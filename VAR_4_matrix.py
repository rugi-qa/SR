n = int(input())  # Задаем размер матрицы
total_step = 0  # Сумму элементов
element_step = 0  # Элементкоторый нужно подсчитать
for i in range(1, n + 1):  # Цикл по строкам
    
    for j in range(1 , n + 1):  # Цикл по столбцам
        if i == j:  # если номер строки равен номеру столбца мы рассчитываем элемент и сумму элементов
            element_step = i * (i + 1)  # рассчет элемента по заданию
            total_step += element_step  # рассчет суммы элементов
        else:  # если номер строки не равен номеру столбца
            element_step = 0  # зануляем элемент по заданию
        print(element_step, end = " ")  # выводим элемент столбца
    print("")  # деламем перенос строки
print("") # делаем отступ (не обязательно)
print(total_step) # выводим сумму элементов диагонали после формирования матри
