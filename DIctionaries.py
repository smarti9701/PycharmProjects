Steve = {'name': 'Steve Martinez', 'age': 44, 'pay': 150000, 'job': 'Agile Coach'}
Eda = {'name': 'Eda Martinez', 'age': 42, 'pay': 150000, 'job': 'Agile Coach'}

print(Steve['name'], Eda['pay'])

print (Steve['name'].split()[-1])

print(Eda['pay']*1.15)




#zipping = joining two lists together
names = ['color', 'height', 'weight']
values = ['black', 65, 250]
print(list(zip(names, values)))




Couple = [Steve, Eda]
for person in Couple:
    print(person['name'], person['pay'], sep=',')
    print(person['name'], person['pay'])
