# Найти корни квадратного уравнения
#Ax² + Bx + C = 0

a, b, c = map(int,input().split())
d = b**2 - 4*a*c
if d > 0:
    print(f'x1 = {round((-b+d**0.5)/(2*a),2)}, x2 = {round((-b-d**0.5)/(2*a),2)}')
elif d == 0:
    print(f'x1 = {round(-b/(2*a)),2}')
else:
    print('Корней нет')

