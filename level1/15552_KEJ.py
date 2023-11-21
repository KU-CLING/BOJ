import sys
i = int(sys.stdin.readline())
numbers = [sys.stdin.readline().rstrip() for i in range(i)]
for i in numbers:
    k = i.split()
    a = int(k[0])
    b = int(k[1])
    print(a+b)