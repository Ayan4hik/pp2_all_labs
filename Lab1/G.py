binary = input()
decimal = 0
for i in range(len(binary)):
    length = len(binary)-i-1
    x = ord(binary[i])-48
    decimal = decimal+ x*(pow(2,length))
print (decimal)