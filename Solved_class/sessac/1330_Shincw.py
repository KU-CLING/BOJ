a, b = input().split()

int_a = int(a)
int_b = int(b)

if (int_a > int_b):
    print(">")
elif (int_a == int_b):
    print("==")
else:
    print("<")