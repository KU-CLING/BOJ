def stringAsNum(a):
    if (a=='Y')|(a=='Z'): return 9;
    elif a=='S': return 7;
    elif a=='V': return 8;
    else:
        return (((ord(a)+1)//3)-20)

S = input()
sum=0
for i in S:
    sum+=stringAsNum(i)+1
print(sum)