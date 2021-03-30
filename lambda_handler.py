from botocore.vendored import requests
import json
#import boto3
#from datetime import datetime
#That's the lambda handler, you can not modify this method
# the parameters from JSON body can be accessed like deviceId = event['deviceId']
#ciudad = 'london'

def lambda_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    ciudad = body['ciudad']
    city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+ciudad
    response = requests.get(city)
    result = response.json()
    code = result['cod']
    if code == 200:
        message = {"ciudad" : ciudad,
            "temperatura":int(result['main']['temp'])- 273.15,
            "viento":result['wind']['speed'],
            "code": "200"
              }
    else:
        message = {
            "code": "202"
              }
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
        }










'''import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


'''