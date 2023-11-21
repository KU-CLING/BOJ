import re
from sys import stdin
while True:
    txt = stdin.readline().rstrip()
    if  txt == '#':
        break;
    else:
        print(len(re.findall('[AEIOUaeiou]', txt)))
        