import sys

while True:
    input = sys.stdin.readline().rstrip()
    if input == '':
        break;
    else:
        A, B = map(int, input.split())
        print(A+B)
