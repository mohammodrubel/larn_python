import requests 
import json 
r = requests.get('https://jsonplaceholder.typicode.com/users/2')
users = json.loads(r.text)

print(users['name'])
print(users['id'])
print(users)
print(r.text)