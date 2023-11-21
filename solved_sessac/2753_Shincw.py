year = input()
year = int(year)

if (year % 4) :
    flag = 0
elif (year % 100) :
    flag = 0
elif (year % 400) :
    flag = 0
else :
    flag = 1

print(flag)