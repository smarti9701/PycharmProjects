Employee1 = ['Steve Martinez', 44, 130000, 'Agile Coach']
Employee2 = ['Eda Martinez', 42, 130000, 'Scrum Master']
print(Employee1)
print(Employee2)

print(Employee2[0], Employee1[0])

print(Employee1[0].split()[-1])  #the negative number refers to the position of the element withing the list item Steve = 0 Martinez = 1 or -1
print(Employee1[0].split()[1])

print(Employee2[2]*1.15)

Company = [Employee1,Employee2] #creates a db with lists
for person in Company:
    print(person)

print(Company[0][0])  #the first reference [0] refers to the row or tuple. the second is the column in the list
print(Company[1][0])


for person in Company:
    print(person[0])