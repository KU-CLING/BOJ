P = list(map(int,input().split()))
A = list(map(int,"1 1 2 2 2 8".split()))
S = []

for i in range(0,6):
    s = A[i] - P[i]
    S.append(s)

S = " ".join(list(map(str,S)))
print(S)