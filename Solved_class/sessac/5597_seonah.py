student = list(range(1,31))


for i in range(28):
    num = input()
    student.remove(int(num))

student = sorted(student)
for i in student:
    print(i)
