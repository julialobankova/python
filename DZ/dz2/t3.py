# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55
n = int(input('Введите число '))
list = []
sum = 0
for i in range(1, n+1):
    list.append(round(((1 + (1/i))**i), 2))
    sum += round(((1+ (1/i))**i), 2)

print('Для n = {}'.format(n)) 
print('Список:')  
print(list)
print('Сумма {}'. format(sum))
