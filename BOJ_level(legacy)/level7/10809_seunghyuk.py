from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
S = input()
for i in alphabet_list:
    print(S.find(i), end = ' ')

    
