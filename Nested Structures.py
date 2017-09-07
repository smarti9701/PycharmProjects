Steve = {'name': {'first': 'Steve', 'last': 'Martinez'},
            'age': 44,
            'job': ['Agile Coach','Management Consultant'],
            'pay': [150000, 200000]}


print(Steve['name'])
print(Steve['name']['last'])
print(Steve['pay'][-1]) #this has no comma
print(Steve['pay'],[-1]) #this one displays both the entire nest, and the additional [-1] as a separate digit because of the comma