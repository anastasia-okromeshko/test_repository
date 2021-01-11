# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
# 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого
# ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
# получить список ключе - использовать метод .keys()
slovar = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(slovar.keys())

i = 0
len_keys = len(keys)

while i < len_keys:
    new_key = f'{keys[i]}{len(keys[i])}'
    slovar[new_key] = slovar.pop(keys[i])
    i += 1
print(slovar)



#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
#'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого
#ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
#получить список ключе - использовать метод .keys()
#(подсказка: создается новы ключ с цифрой в конце,
#старый удаляется)
slovar = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(slovar.keys())

i = 0
len_keys = len(keys)

for tep in keys:
    new_key = f'{keys[i]}{len(keys[i])}'
    slovar[new_key] = slovar.pop(keys[i])
    i += 1
print(slovar)
