n, x = map(int, input().split())
nlist = list(map(int, input().split()))

for i in range (n):
    if nlist[i] < x:
        print(nlist[i], end = ' ')