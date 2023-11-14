import sys

N = sys.stdin.readline().rstrip()
N = int(N)
for i in range(1,N+1):
    for j in range(N, i, -1): ## N-번 출력
        print(" ", end = "")
    for k in range(1,i+1): ## i번 출력
        print("*", end = '')
    print()
