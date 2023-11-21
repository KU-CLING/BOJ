x = input()
x = int(x)

y = input()
y = int(y)

if (x * y > 0) :
    flag = 1
else :
    flag = 0

if (flag) :
    if (x > 0) :
        print('1')
    else :
        print('3')
else :
    if (x > 0) :
        print('4')
    else :
        print('2')