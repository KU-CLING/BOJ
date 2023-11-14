import re
from sys import stdin
from string import ascii_lowercase

alpha = list(ascii_lowercase)

def noVowels(text):
    if re.search('[AEIOUaeiou]', text) == None:
        return 0;
    else:
        return 1;

def rep_3times(text):
    if re.search('[AEIOUaeiou]{3,}', text) != None:
        return 0;
    elif re.search('[^AEIOUaeiou]{3,}',text) != None:
        return 0;
    else: 
        return 1;

def rep_2times(text):
    text = text.replace('ee', '')
    text = text.replace('oo', '')
    for i in alpha:
        if re.search('%s{2,}' %i, text) !=None:
            return 0;
    return 1;    
    



while True:
    txt = stdin.readline().rstrip()
    if txt == 'end':
        break;
    else:
        test1 = noVowels(txt)
        test2 = rep_3times(txt)
        test3 = rep_2times(txt)
        if test1&test2&test3 == 1:
            print("<%s> is acceptable." %txt)
        else:
            print('<%s> is not acceptable.' %txt)
