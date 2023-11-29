num = input()
num = num.split()
num[0] = int(num[0])
num[1] = int(num[1])
if num[0] > num[1] :
    print(">")
elif num[0] < num[1] :
    print("<")
else :
    print("==")