Employee1 = ['Steve Martinez', 44, 150000, 'Agile Coach']
Employee2 = ['Eda Martinez', 42, 130000, 'Scrum Master']
print(Employee1)
print(Employee2)

print(Employee2[0], Employee1[0])

print(Employee1[0].split()[-1])  #the negative number refers to the position of the element withing the list item Steve = 0 Martinez = 1 or -1
print(Employee1[0].split()[1])

print(Employee2[2]*1.15)

people = [Employee1, Employee2] #creates a db with lists
for person in people:
    print(person)

print(people[0][0])  #the first reference [0] refers to the row or tuple. the second is the column in the list
print(people[1][0])


for person in people:  #this will list only the first column
    print(person[0])

for person in people:  #to check pay for each person or record
    print(person[2])

pays = [person[2] for person in people]  #prints pay for each record
print(pays)

pays = map((lambda x:x[2]), people)    #A use of map here would be if you start with a list
# of strings instead of a single string - map can listify all of them individually
# f = lambda x, y : x + y
# #f(1,1)
#  2
#list(pays)  this command from the tutorial doesn't show anything because it needs the print() command
print(list(pays))

print(sum(person[2] for person in people))

people.append(['Jazzy', 20, 10000, 'Barista'])
print(people)
print(Employee1)
print(Employee2)
#print(Employee3) - you can't bring up Employee3 though because it hasn't been created
print(len(people)) #produces the number of records
print(people[-1][0]) #brings up the first list item going backwards - -1 and provides the first "element" in that sublist