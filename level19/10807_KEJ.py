import sys
num1 = int(input())
data = list(map(int, sys.stdin.readline().split()))
num2 = int(input())
num3 = 0
for i in data:
    if i == num2:
        num3+=1
print(num3)