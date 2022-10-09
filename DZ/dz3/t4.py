# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# По условию задачи:
def binarysystem (num):
    numsys = 2
    new_num = ''
    while num > 0:
        new_num = str(num % numsys) + new_num
        num //= numsys
    return new_num  
number = int(input('Введите число '))
print(binarysystem(number))      



#доп системы исчеления
def system_1_9(num, numsys ):
    new_num = ''
    while num > 0:
        new_num = str(num % numsys) + new_num
        num //= numsys
    return new_num 

number = int(input('Введите число '))
system = int(input('Систему исчесления от 2 до 9 '))
print(system_1_9(number, system))

 
