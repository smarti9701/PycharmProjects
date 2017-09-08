steve = dict(name='Steve Martinez', age=44, job='unemployed', pay=0)
eda = dict(name='Eda Martinez', age=42, job='Scrum Master', pay=130000)
jazzy = dict(name='Jazzy Martinez', age=20, job='student''lifetime employee', pay=10)
amber = dict(name='Amber Martinez', age=15, job='student', pay=0)

print(steve)

db={}
db['steve']=steve
db['eda']=eda
db['jazzy']=jazzy
db['amber']=amber

print(db['amber']['job'])
print(db['jazzy']['pay'])

import pprint
pprint.pprint(steve)


for key in db:
    print(key, '=>', db[key]['name'])
    #print(steve)
for key in db:
    print(key, '=>', db[key]['pay'])

for key in db:
    print(db[key]['name'].split()[-1]) #3print all the last names

for key in db:
    print(db[key]['job'].split())

for record in db.values():
    print(record['pay'])
