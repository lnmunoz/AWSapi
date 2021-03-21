import json

def lambda_handler(event, context):
    cityName = event['queryStringParameters']['cityName']

    city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+cityName

    print(city)
    response = requests.get(city)
    result = response.json()

    responseObjet = {}
    responseObjet['message'] = {'Gracias por utilizar la API'}

    responseObjet['statusCode'] = 200
    responseObjet['Headers'] {}
    responseObjet['body'] = result

    return responseObjet



