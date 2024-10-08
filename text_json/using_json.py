# JSON is Javascript Object Notation - it is NOT Jvascript, it is plain text
import json # this library is part of Python
# rules of JSON: everything is in double quotes except numbers and boolean

if __name__ == '__main__':
    '''Here is a tuple of dictionaries'''
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )  
    # we may convert this structure to plain text
    j = json.dumps(creatures_t) # serialize the structure to text
    print(j, type(j))
    # We can also covert correctly-formatted JSON back into a structure
    s = json.loads(j)
    print(s, type(s))


    # some JSON
    x = [{"creature": "Albatros", "count": 1, "cost": 120.99}, {"creature": "Bear", "count": 5, "cost": 323.56}, {"creature": "Carp", "count": 120, "cost": 87.0}, {"creature": "Deer", "count": 121, "cost": 12.99}, {"creature": "Elk", "count": 7, "cost": 73.47}]
