#Даны действительные числа x и y. Получить (|x|-|y|)/1+|xy|
import math
x=2
y=4
c= (math.fabs(x)- math.fabs(y))/ (1+ math.fabs(x*y))
print ("модуль:", c)
