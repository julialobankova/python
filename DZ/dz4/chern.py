# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0


from random import randint, choice, uniform

def roots_equ(a, k, sign):
        with open("new.txt", "a", encoding="utf-8") as my_f:
            while k >= 1:
                my_f.write(f"({a}x ** {k})){sign}")
                k=k-1
                a = round(uniform(0, 10), 2)
                sign = choice('+-')
            my_f.write(f" {a}\n")
for i in range(3):
    SL = []
    SL.append(randint(1, 5))
    k = choice(SL)
    sign = choice('+-')
    a = round(uniform(0, 10), 2)
    print(a,k,sign)
    roots_equ(a,k,sign)