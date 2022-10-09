# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import numbers
sum = 0
numbers = list(map(int, input('Введите через пробел числа ').split()))
print(numbers)
for i in range(len(numbers)):
    if i % 2:
        sum += numbers[i] 
print(sum)