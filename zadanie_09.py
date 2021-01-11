# Для каждого натурального числа в промежутке от m до
# n вывести все делители, кроме единицы и самого
# числа. m и n вводятся с клавиатуры.
m = int(input("Минимум: "))
n = int(input("Максимум: "))
while m <= n:
    c = 0
    for i in range(2,m+1):
        if m%i == 0:
            c += 1
    if c >= 2:
        print(m,':',end=' ')
        for i in range(i-1,1,-1):
            if m%i == 0:
                print(i,end=' ')
        print()
    m += 1
