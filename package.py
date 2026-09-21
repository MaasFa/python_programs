import requests

response = requests.get('https://github.com/MaasFa')

print(response.status_code) #output: 200
 

