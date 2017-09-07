Steve = {'name': 'Steve Martinez', 'age': 44, 'pay': 150000, 'job': 'Agile Coach'}
Eda = {'name': 'Eda Martinez', 'age': 42, 'pay': 150000, 'job': 'Agile Coach'}

print(Steve['name'], Eda['pay'])

print(Steve['name'].split()[-1])

print(Eda['pay'] * 1.15)

# zipping = joining two lists together
 #names = ['color', 'height', 'weight']
 #values = ['black', 65, 250]
 #print(list(zip(names, values)))

people = [Steve, Eda]
for person in people:  # this identifies and sets rule up for each list item to be tied to "person"
    #print(person['name'], person['pay'], sep=',')  # these two print statements do the exact same output
    print(person['name'], person['pay'])
#for person in Couple:
    if person['name'] == 'Steve Martinez': #since the key is 'name', then I have to use the name indicated for 'name'
        print(Steve['pay'])

    #else:
        #print('done')


input("Please enter Employee's name: ")
for person in people:
   #if input == person['name']:
   if person['name'] == Steve:
        print(person['pay'])


    #names = person['name']
    #for person in people:
        #print([names])

list(map((lambda x:x['name']), people))

sum(person['pay'] for person in people)
