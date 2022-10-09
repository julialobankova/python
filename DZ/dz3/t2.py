# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint

def arrayrand(lengthlist):
    numbers = []
    for i in range(lengthlist):
        numbers.append(randint(0, 10))
    return numbers

def prodpair(array):
    pr_list = []
    sum = 0
    p = len(array)
    for i in range(p//2):
        sum = array[i]*array[-i-1]
        pr_list.append(sum)
    return pr_list

work_list = arrayrand(int(input('Введите длину списка ')))
print(work_list)
print(prodpair(work_list))

    

