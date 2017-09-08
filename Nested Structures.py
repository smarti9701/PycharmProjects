Steve = {'name': {'first': 'Steve', 'last': 'Martinez'},
            'age': 44,
            'job': ['Agile Coach','Management Consultant'],
            'pay': [150000, 200000]}


print(Steve['name'])
print(Steve['name']['last'])
print(Steve['pay'][-1]) #this has no comma
print(Steve['pay'],[-1]) #this one displays both the entire nest, and the additional [-1] as a separate digit because of the comma

# almost like a SQL query
for job in Steve['job']: #for item in Steve['job']
    print(job)

print(Steve['job'][-1])

Steve['job'].append('Orgasm Donor')
print(Steve['job'][2])

print(Steve)