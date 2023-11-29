T = int(input())
for i in range(T):
    R, string = input().split()
    R = int(R)
    for j in string:
        for k in range(R):
            print(j, end = '')
    print()
 
 