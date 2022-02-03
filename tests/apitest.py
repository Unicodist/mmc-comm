import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE+'/api/user/1/', {'firstname':'Ashish','lastname':'Neupane','address':'Birtamode','phone':'676767','password':'secret123'})
response = requests.post(BASE+'/api/login/',{'phone':9880769907,'password':'secret123'})
# response = requests.get(BASE+'api/user/1')
print(response.json())
# response = requests.put(BASE+"api/user", {'fname': 'Ashish', 'lname': 'Neupane', 'address': 'Birtamode', 'phone': '9880769907'})