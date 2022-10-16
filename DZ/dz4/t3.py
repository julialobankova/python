# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


from random import randrange

def list_rand_nums(count: int):
    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums

listm = list_rand_nums(6)  
print(listm)


def get_uniq_nums (list_num):
    uniq_num = []
    for i in list_num:
        count = list_num.count(i)
        if count == 1:
            uniq_num.append(i)
    return uniq_num

print(get_uniq_nums(listm))


        
    





