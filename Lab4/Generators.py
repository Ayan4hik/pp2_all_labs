print("Ввeдите номер задания: ")
a = int(input())

if a == 1:
    n = int(input())
    for i in range(n):
        print (str(i**2), end=' ')

if a == 2:
    n = int(input())
    for i in range(n):
        if i%2==0:
            print (str(i), end=' ')

if a == 3:
    def div12(i):
            if i%12==0:
                return i
            else:
                return "None"
    print("Ввeдите два числа в строку")
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    for i in range(a,b):
        c = div12(i)
        if c != "None":
            print (str(c), end=' ')

if a == 4:
    print("Ввeдите два числа в строку")
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    def squares(i):
        return i**2
    for i in range(a,b):
        print(squares(i), end=' ')

if a == 5:
    n = int(input())
    while n>=0:
        print(n, end=' ')
        n-=1