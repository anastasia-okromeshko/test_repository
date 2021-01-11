# Дан список. Создать новы список, сдвинуты на 1
# элемент влево Пример:12345 -> 23451


spisok = [ 1, 2, 3, 4, 5]

spisok_len = len(spisok)

new_spisok = []

i=1
while i< spisok_len:
    new_spisok.append(spisok[i])
    i += 1

new_spisok.append(spisok[0])
print(new_spisok)
