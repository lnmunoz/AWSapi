import requests
import json

url = 'https://ug0byqxud1.execute-api.us-east-1.amazonaws.com/Testeo/PostApiClima'
myvar = {
    "ciudad":"moscu"
    }

x = requests.post('https://ug0byqxud1.execute-api.us-east-1.amazonaws.com/production/PostApiClima', json={"ciudad":"tokio"})

result = x.json()

print(result)