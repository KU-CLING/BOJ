N, M = input().split()

N = int(N)
M = int(M)

diff = N-M
if diff > 0:
    print(diff)
else:
    print(-diff)