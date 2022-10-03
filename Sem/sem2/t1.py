# Поиск элемента в строке 
text = "Эники беники ели варенники"
print(text)
simvol = input('Введите символ, который хотите найти ')
result = 0
for i in text:
    if i == simvol:
        result += 1
print(result)
    
