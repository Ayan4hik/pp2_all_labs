import math
from math import tan
print("Введите номер задания: ")
a = int(input())

if a == 1:
    deg = float(input())
    rad = deg/(180/math.pi)
    print(rad)
if a == 2:
    print("Введите высоту: ")
    h = float(input())
    print("Введите первое основание: ")
    a = float(input())
    print("Введите второе основание: ")
    b = float(input())
    S = (a+b)/2*h
    print(S)

if a == 3:
    print("Введите количество углов: ")
    n = int(input())
    print("Введите длину одной стороны: ")
    a = float(input())
    def ctg(x):
        return 1/tan(x)
    S = (n/4)*a**2*ctg(math.pi/n) #the formula is real for any regular polygon
    print(S)

if a == 4:
    print("Введите высоту: ")
    h = float(input())
    print("Введите основание: ")
    a = float(input())
    S = a*h
    print(S)