while True:
    try:
        i = input()
        k = i.split()
        print(int(k[0])+int(k[1]))
    except:
        break