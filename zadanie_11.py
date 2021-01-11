#Дан список целых чисел. Подсчитать сколько четных чисел в списке
list = [1, 2, 3, 4, 5]
a_list = len(list)
i = 0
even = 0
while i < a_list:
    if list[i]  % 2 == 0:
        even += 1
    i += 1
print(even)
