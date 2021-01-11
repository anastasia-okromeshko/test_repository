#  В списке целых случайных чисел с количеством
#  элементов n определить максимальное число и
#  заменить им все четные по значению элементы.

from random import randint

list = []
for i in range(50):
    list.append(randint(0, 50))
print (list)

maximum = max(list)
print(maximum)
a = 0

for i in list:
    if i % 2 == 0:
        list[a] = maximum
    a += 1
print(list)
