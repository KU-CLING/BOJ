N = int(input())

for i in range(1,N):
    print(" "*(N-i)+"*"*(2*i-1))

for i in range(N,2*N):
    print(" "*(i-N)+"*"*(4*N-2*i-1))

