import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+'/api/user/'+str(1))
print(response.json())
# response = requests.put(BASE+"api/user", {'fname': 'Ashish', 'lname': 'Neupane', 'address': 'Birtamode', 'phone': '9880769907'})