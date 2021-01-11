# Написать генератор песенки «TEN green bottles
# hanging on the wall».
# В песенке вместо цифр должны быть именно слова,
# обозначающие цифры, т.е. TEN, NINE, EIGHT, etc.

print("TEN green bottles hanging on the wall")
list = [ "NINE", "EIGHT", "SEVEN", "SIX", "FIVE", "FOUR", "THREE", "TWO", "ONE"]
a_list = len(list)
a = "green bottles hanging on the wall"
b = "And if one green bottle should accidentally fall.\nThere‛ll be..\n"
i = 0
e = 0
while i < a_list:
    print(b, list[e], a)
    i += 1
    e += 1

print("NO", a)
