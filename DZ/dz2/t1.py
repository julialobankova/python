#Для натурального n создать словарь индекс-значение, 
#состоящий из элементов последовательности 3n + 1.
#Пример:
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число '))
def dictionary(n):
    list = []
    i = 1
    while (i <= n):
        list = ['{}: {}'.format(i, 3*i+1)]
        return list
print(list)