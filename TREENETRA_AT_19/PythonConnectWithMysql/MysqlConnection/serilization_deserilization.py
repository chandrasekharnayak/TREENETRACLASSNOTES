import json

'''json_reader = open('data.json','r')
json_data = json_reader.read()'''


#loads :- json string --- python object
'''json_loads = json.loads(json_data)
print(json_loads)
print(type(json_loads))'''

#dumps :-

import python_data

store = python_data.data

json_dumps = json.dumps(store)
print(type(json_dumps))