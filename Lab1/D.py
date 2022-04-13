def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

n=float(input())
s = str(input())

if s == "k":
    a=n/1024
    l = int(input())
    a = toFixed(a,l)
elif s == "b":
    a=n*1024

print(a)
