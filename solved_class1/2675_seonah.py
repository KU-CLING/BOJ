t = int(input())

for i in range(t):
    r, string = input().split(" ")
    result = ""
    for char in string:
        result += char * int(r)
    print(result)
