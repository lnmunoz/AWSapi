import urllib3 
import json
import logging

logging.basicConfig(level=logging.INFO)

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
    #logging.basicConfig(filename="registro.log", level=logging.DEBUG)
    logging.info(code)
    
    if code == 200:
        message = {"ciudad" : ciudad,
            "temperatura":int(result['main']['temp'])- 273.15,
            "viento":result['wind']['speed']
              }
        statuscode = '200'
        logging.info('Mensaje exitoso')
    else:
        message = { "Error" : "Error en parametro"
              }
        statuscode = '400'
        logging.info('Error en parametro')
    return {
        'statusCode': statuscode,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
        }
