import sys

rawlist = []
while True:
    input = sys.stdin.readline().rstrip()
    if input == '':
        break;
    else: 
        string = input.rstrip()
        for i in range(len(string)):
            rawlist.append((string[i]))
        rawstr = ''.join(rawlist)
        print(rawstr)
        rawlist = []
    
