import sys

while True:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if A==0 & B == 0:
        break;
    else:
        print(A+B)

