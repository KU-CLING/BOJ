S = input()
L = "ABC DEF GHI JKL MNO PQRS TUV WXYZ".split()
N = []

for s in S:
    for i in L:
        if s in i:
            N.append(3+L.index(i))
        else:
            pass

print(sum(N))