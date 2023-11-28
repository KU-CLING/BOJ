while True:
    i = input()
    k = i.split()
    if i == '0 0':
        break
    print(int(k[0])+int(k[1]))