t = int(input())

for i in range(t) :
    num = input()
    num = num.split()
    num[0] = int(num[0])
    num[1] = int(num[1])
    print(num[0] + num[1])