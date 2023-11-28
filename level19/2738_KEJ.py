# 행렬 덧셈
import sys
rows, cols = map(int, sys.stdin.readline().split())
mat1 = []
mat2 = []
for i in range(rows):
    mat1.append(list(map(int, sys.stdin.readline().split())))
for i in range(rows):
    mat2.append(list(map(int, sys.stdin.readline().split())))

answer = []

for r in range(rows):
    answer2 = []
    for c in range(cols):
        a = mat1[r][c]+mat2[r][c]
        answer2.append(a)
    answer.append(answer2)

for l in answer:
    print(' '.join(str(s) for s in l))
        