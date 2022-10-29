# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#КОД ДО:
# n = int(input('Введите число '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i       
#     print(' {} '.format(factorial), end="")


n=int(input("Введите число:"))
fact = lambda n: 1 if n == 0 else n * fact(n - 1)
print(fact(n))