line= input().split()
distance = int(line[0])
num = int(line[1])
check = "Prime"

if distance > 1:
    for i in range(2, int(distance/2)+1):
         if (distance % i) == 0:
                check = "Not"
                break
    else:
        check = "Prime"

else:
    check = "Not"

if distance<=500:
    if check == "Prime":
        if (num%2)==0:
            print("Good job!")
        else:
            print("Try next time!")
    else:
        print("Try next time!")
else:
    print("Try next time!")