import sys
def input():
    return sys.stdin.readline()

T = int(input().rstrip())
for i in range(T):
     A, B = map(int, input().split(" "))
     print("Case #%d:" %(i+1) ,end = " ")
     print(A+B)

