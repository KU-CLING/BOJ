def add_input():
    a, b = input().split()
    print(int(a)+int(b))

while(1):
    try:
        add_input()
    except EOFError:
        break

