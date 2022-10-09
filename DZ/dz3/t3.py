from random import sample

def array1(count):
    if count < 1:
        return 'Error'
    list_elements = sample(range(1, count * 3), count)
    return list_elements

def product_num(new_array):  # произведение пар чисел списка
    res = 0
    length = len(new_array)
    res_list = []
    for i in range(length//2):
        res = new_array[i] * new_array[length - i - 1]
        res_list.append(res)
    if length % 2:
        res_list.append(new_array[length//2])
    return res_list

my_list = array1(int(input('Введите длину списка: ')))
print(my_list)
if my_list != 'Error':
    print(product_num(my_list))
else:
    print('List creation error')