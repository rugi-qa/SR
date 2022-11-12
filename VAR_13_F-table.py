# Способ 1:
# x = [-0.7; 0.7] , h = 0.1
import math
y = 0

a = float(input('Введите начлао множества: '))  # -0.7
b = float(input('Введите конец множества: '))  # 0.7
h = float(input('Введите шаг: '))  # 0.1
x = a
while a <= x <= b:
    y = math.log((1 + x) / (1 - x))
     # x = x + h
    print("При x =", round(x,2), 'функция y =',round(y,2))
    x += h

# Способ 2:
y = 0
x = a
count_y = math.ceil((b - a) / h) + 1
print(count_y)
for _ in range (count_y):
    y = math.log((1 + x) / (1 - x))
     # x = x + h
    print("При x =", round(x,2), 'функция y =',round(y,2))
    x += h
