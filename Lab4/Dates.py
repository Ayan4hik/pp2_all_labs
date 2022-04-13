from datetime import date, timedelta, datetime
now = datetime.now()
print("Введите номер задания: ")
n = int(input())
if n==1:
    day5 = now - timedelta(days=5)
    print(day5)
if n==2:
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)
    print("Yesterday: "+ str(yesterday))
    print("Today: "+ str(now))
    print("Tomorrow: "+ str(tomorrow))

if n==3:
    print(now.strftime("%y-%m-%d %H:%M:%S"))

if n==4:
    print("Вводите в формате ниже")
    print("год-месяц-день час:минута:секунда")
    date1 = datetime.strptime(input(), "%y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(input(), "%y-%m-%d %H:%M:%S")
    diff= date2-date1
    sec=diff.days * 24 * 3600 + diff.seconds
    if sec<0:
        sec = -sec
    print(sec)