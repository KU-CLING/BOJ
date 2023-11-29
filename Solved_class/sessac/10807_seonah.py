length = input()
int_list  = input().split()
v = input()

cnt = 0
for n in int_list:
    if n == v:
        cnt += 1

print(cnt)