#How to merge two dictionaries

x = {'Katy': 44, 'Dom': 55}
y = {'Hector': 10, 'Jesse':7}

z = {**x, **y}

print (z)