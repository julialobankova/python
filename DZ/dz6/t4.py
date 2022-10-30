# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

input_list = input('Введите выражанение для посчета: ').split()
output = []
stack = []
for elem in input_list:
    if elem.isdigit():
        output.append(elem)
    elif elem == '(': #помещаем в стек
        stack.append(elem)
    elif elem == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop()) #забирает последний элемент из stack и помезает в output            
        if not stack:
            print('Не согласованные скобки')
            exit()    
        stack.pop()
    elif elem in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            output.append(stack.pop())           
        stack.append(elem)
    elif elem in ['+', '-']:
        while stack and stack[-1] in ['*', '/', '+', '-']:
            output.append(stack.pop())           
        stack.append(elem) 

    else:
        print('НЕ распознанный знак')
        exit()
while stack:
    if stack[-1] not in ['*', '/', '+', '-']:
        exit()
    output.append(stack.pop())

res = []
for elem2 in output:
    if elem2.isdigit():
        res.append(int(elem2))
    else:
        b = res.pop()
        a = res.pop()
        if elem2 == '+':
            res.append(a + b)
        elif elem2 == '-':
            res.append(a - b)
        elif elem2 == '*':
            res.append(a * b)
        elif elem2 == '/':
            res.append(a / b)
print(res[0])

