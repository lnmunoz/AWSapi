from botocore.vendored import requests
import json


def lambda_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    ciudad = body['ciudad']
    city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+ciudad
    response = requests.get(city)
    result = response.json()
    
    message = {"ciudad" : ciudad,
            "Temperatura":int(result['main']['temp'])- 273.15,
            "Presión":result['main']['pressure'],
            "Humedad":result['main']['humidity']
            "Viento":result['wind']['speed']
              }
              
              
    return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(message)
            }