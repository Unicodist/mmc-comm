import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE+'/api/user/1/', {'firstname':'Ashish','lastname':'Neupane','address':'Birtamode','phone':'7674673','password':'secret123'})
# response = requests.post(BASE+'/api/login/',{'phone':786567,'password':'secret123'})
# response = requests.get(BASE+'api/user/1')
print(response.json())
