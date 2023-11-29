from sys import stdin

T = int(stdin.readline().rstrip())
for i in range(T):
    string = stdin.readline().rstrip()
    print("%s%s" %(string[0], string[-1]))
