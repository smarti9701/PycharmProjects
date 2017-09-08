steve = dict(name='Steve', age=44, job='unemployed', pay=0)
eda = dict(name='Eda', age=42, job='Scrum Master', pay=130000)
jazzy = dict(name='Jazzy', age=20, job='student''lifetime employee', pay=10)
amber = dict(name='Amber', age=15, job='student', pay=0)

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