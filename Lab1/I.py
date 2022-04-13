n=int(input())
for i in range(n):
    adress=input()
    l = len(adress)
    dom = adress[l-10:]
    if dom=="@gmail.com":
        print(adress[:l-10])
