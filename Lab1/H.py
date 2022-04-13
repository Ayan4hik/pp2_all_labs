
txt = input()
char = input()
f=""
l=""


for i in range(len(txt)):
    if char == txt[i]:
        f = str(i)
        break
for i in range(len(txt)):
    if char == txt[i]:
        l = str(i)
if f!=l:
    print (f, l)
else:
    print(l)