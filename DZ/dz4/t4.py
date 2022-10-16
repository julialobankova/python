from random import randint, choice

def poly(a, k, sign):
    with open("new1.txt", "a", encoding="utf-8") as my_f:
        while k >= 0:
            my_f.write(f"({a}x ** {k})){sign}")
            k = k - 1
            if k == 0:
                break
            a = randint(0, 100)
            sign = choice('+-')
        my_f.write(f" {a}\n")


k1 = int(input())
a1 = randint(0, 100)
sign1 = choice('+-') 
poly(a1, k1, sign1)



  

