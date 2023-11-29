S = input()
S = S.split()

A = int(S[0][::-1])
B = int(S[1][::-1])

if A>B:
    print(A)
else:
    print(B)

