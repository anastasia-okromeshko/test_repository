# Для заданного числа N составьте программу
# вычисления суммы S=1+1/2+1/3+1/4+...+1/N, где N –
# натуральное число.
n = int(input())
s = 0.0
for i in range(1, n + 1):
    s += 1.0 / i

print(s)
