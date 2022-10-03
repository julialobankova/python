#Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды

second = int(input('Введите секунды '))
minut = 0
hours = 0 
day = 0

minut = int(second/60)
hours = int(minut/60)
day = int(hours/24)
second1 = second%60
print('{} дней {} часов {} минут {} секунд'.format(day, hours, minut, second1))
