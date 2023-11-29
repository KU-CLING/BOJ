unique_number = input()
numbers = unique_number.split(' ')

val_number = 0
for number in numbers:
    number = int(number)
    val_number += number**2

val_number = val_number % 10
print(val_number)
    
