from botocore.vendored import requests
import json


def lambda_handler(event, context):
    print('event:', json.dumps(event))

    cityName = event['cityName']
    print(event)
    #cityName = 'madrid'
    city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+cityName

    #print(city)
    response = requests.get(city)
    result = response.json()
    
    cityResponse = {}
    cityResponse['cityName'] = cityName
    

    responseObjet = {}
    #responseObjet['message'] = {'Gracias por utilizar la API'}
    responseObjet['statusCode'] = 200
    #responseObjet['headers'] {}
    responseObjet['body'] = result

    return responseObjet
    #return json.dumps(event)