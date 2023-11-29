T = int(input())
sums = []
for i in range(T):
    A, B = input().split(" ")
    A = int(A); B = int(B)
    sums.append(A+B)
for i in range(T):
    print(sums[i])

# T = int(input())
# for i in list(input() for _ in range(T)):
#     a, b = map(int, i.split())
#     print(a,b)

