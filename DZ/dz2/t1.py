# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите вещесвенное число '))
sum = 0
power = len(str(number)) - 2
number *= 10 ** power
while number:
    sum += number % 10
    number //= 10
print(int(sum))