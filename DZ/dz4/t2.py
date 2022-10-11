#Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


def multi (n):
   i = 2
   multi = []
   while i * i <= n:
       while n % i == 0:
           multi.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       multi.append(n)
   return multi
number = int(input())
mul = map(int, multi(number))
print(list((mul)))