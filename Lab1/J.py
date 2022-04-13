line=input().split()
output = ""
for i in range(len(line)):
    word = line[i]
    if len(word)>=3:
        output += word+" "
print (output)
