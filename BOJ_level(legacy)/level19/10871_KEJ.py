import sys
n, x = map(int,sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
answer = []
for k in data:
    if k<x:
        answer.append(k)    
print(' '.join(str(s) for s in answer))