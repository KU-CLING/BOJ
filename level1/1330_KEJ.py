i = input()
s = i.split()
a = int(s[0])
b = int(s[1])
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')