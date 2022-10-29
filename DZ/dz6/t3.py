#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#Примеры:
#5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# ДО:
# n = int(input('Введите число '))
# list = []
# for i in range(-n, n+1):
#     list.append(i)
# print(list)    

n = int(input('Введите число '))
squares = [i for i in range(- n, n+1)]
print(squares)


