# Напишите программу, которая на вход принимает 5 чисел (можно списком)
# и находит максимальное из них.
# Примеры:
# 1. 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

numbers = list(map(int, input().split()))
max = 0
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print('{}, -> {}'.format(numbers, max))
