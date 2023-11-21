wrong_answer = input()

answer = ''
for letter in wrong_answer:
    if letter.isupper():
        answer += letter.lower()
    elif letter.islower():
        answer += letter.upper()
    else:
        answer += letter

print(answer)


        
