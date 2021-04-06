import urllib3 
import json
import logging

def lambda_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    ciudad = body['ciudad']
    city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+ciudad
    #response = requests.get(city)
    http = urllib3.PoolManager()
    response = http.request('GET',city)
    result = json.loads(response.data)
    code = result['cod']
    print (code)
    logging.basicConfig(filename="registro.log", level=logging.DEBUG)
    logging.debug(code)
    
    if code == 200:
        message = {"ciudad" : ciudad,
            "temperatura":int(result['main']['temp'])- 273.15,
            "viento":result['wind']['speed'],
            "code": "200"
              }
        statuscode = '200'
    else:
        message = { "Error" : "Error en parametro"
              }
        statuscode = '202'
    return {
        'statusCode': statuscode,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
        }
