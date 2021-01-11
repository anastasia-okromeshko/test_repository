#Дано число. На ти сумму и произведение его цифр.
number = int(input())

suma = 0
mult = 1

while number > 0:
    digit = number % 10
    suma = suma + digit
    mult = mult * digit
    number = number // 10

print("Сумма:", suma)
print("Произведение:", mult)
