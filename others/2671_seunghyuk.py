import re
sound = input()
#각 단위는 (100+1+)|(01)
pattern= re.compile(r'^(100+1+|01)+$')
if pattern.match(sound):
    print("SUBMARINE")
else:
    print('NOISE')