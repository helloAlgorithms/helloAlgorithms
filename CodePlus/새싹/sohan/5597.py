students = []
table = []
for index in range(0, 28):
    number = int(input())
    students.append(number)
    table.append(index + 1)
table.append(29)
table.append(30)
table.reverse()
sorted_student = sorted(students, reverse = True)
num = 1;
while len(sorted_student):
    if table[len(table) - 1] == sorted_student[len(sorted_student) - 1] : 
        sorted_student.pop()
        table.pop()
    else : print(table.pop())
while (len(table)):
    print(table.pop())
