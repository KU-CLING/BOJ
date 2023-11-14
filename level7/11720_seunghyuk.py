import sys

N = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()
sum = 0
str_list = [int(string[i]) for i in range(N)]
for i in range(N):
    sum +=str_list[i]
print(sum)