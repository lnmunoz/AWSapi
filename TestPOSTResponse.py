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
    print(body)
    return{
            'statusCode': 200,
            'body': ciudad
    }
