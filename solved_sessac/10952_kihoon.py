num_list = list()
num = 0

while num != "0 0" :
    num = input()
    num_list.append(num)

for num in num_list :
    if num == "0 0" :
        break
    num = num.split()
    num[0] = int(num[0])
    num[1] = int(num[1])
    print(num[0] + num[1])