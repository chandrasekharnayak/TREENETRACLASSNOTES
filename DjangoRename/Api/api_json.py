import json

# json.dumps()--- conver dict to byte strem(json-string)
# json.loads()---- convert byte strem to dictionary

payload = {'name': 'morpheus','job': 'leader'}
data = json.dumps(payload)
print(type(data))
print(data)
