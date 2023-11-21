T = int(input())

while T>0:

    T = T-1
    RS = input()
    RS = RS.split()
    R = int(RS[0])
    S = RS[1]

    L = []
    for s in S:
        L.append(s*R)

    P = "".join(L)
    print(P)