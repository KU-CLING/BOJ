N, M = input().split()
N = int(N)
M = int(M)

A = list()
B = list()
C = list()

# Matrix A
for i in range(N):
    temp = list()
    elements = input().split()
    for j in range(M):      
        temp.append(int(elements[j]))
    A.append(temp)
          
# Matrix B
for i in range(N):
    temp = list()
    elements = input().split()
    for j in range(M):      
        temp.append(int(elements[j]))
    B.append(temp)


# Matrix C
for i in range(N):
    temp = list()
    for j in range(M):
        temp.append(str(A[i][j]+B[i][j]))
    
    print(' '.join(temp))