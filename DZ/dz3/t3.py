# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
def arrayrand(lengthlist):
    numbers = []
    for i in range(lengthlist):
        numbers.append(random.uniform(0, 10))
    return numbers

def diff(array):
    mylist = []
    for i in array:
            mylist.append(round(i%1,2))
    print(mylist)
    print(f"-> {max(mylist) - min(mylist)}")


work_array = arrayrand(5)
diff(work_array)

