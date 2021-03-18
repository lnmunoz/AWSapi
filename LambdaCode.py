# import libraries here

from botocore.vendored import requests

from datetime import datetime

def lambda_handler(event, context):

# Get the current date and time in yy–mm-dd hours:minutes:seconds format
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')

    ciudad = 'london'

    city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+ciudad

    print(city)
    response = requests.get(city)
    result = response.json()



# API call
    #response = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Washington,us&APPID=53d6430c1eccacb54e827045d1aee3d3')

# Check if the request completed successfully
    return {
        'statusCode': 200,
        'body': result
    }