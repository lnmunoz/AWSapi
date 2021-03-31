import requests
import json
import unicodedata


def quitartil(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)

print("Bienvenido a consultor de tiempo")
ciudad = str(input("Ingrese nombre de ciudad: "))
#print (ciudad)
ciudad = quitartil(ciudad)
#print(ciudad)
#Funcion para normalizar el nombre de la ciudad y quitar tildes





#ciudad = input("Ingrese nombre de ciudad: ")

#url = "https://euic8aetta.execute-api.us-east-1.amazonaws.com/dev/LambdaClima/crea"

url = "https://2fcs79r6k1.execute-api.us-east-1.amazonaws.com/dev/LambdaClima/crea"

payload= '{\r\n    \"ciudad\":\"'+ciudad+'\"\r\n    }'


#payload="{\r\n    \"ciudad\":\"cordoba\"\r\n    }"

#print(pay)

headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response)

salida = response.json()
#print (salida)
code = salida['code']
#print(code)
if code == '200':
  print
  print("------------------------------------------------------")
  print("Datos del tiempo en "+ciudad+" son: ")
  print("Temperatura: "+str(salida['temperatura']))
  print("Viento: "+str(salida['viento']))
  print("Gracias por utilizar el servicio")
  print("------------------------------------------------------")
else:
  print("Parametro incorrecto")