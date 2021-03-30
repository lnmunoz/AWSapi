import requests
import json
print("Bienvenido a consultor de tiempo")
ciudad = str(input("Ingrese nombre de ciudad: "))

#ciudad = input("Ingrese nombre de ciudad: ")

#url = "https://euic8aetta.execute-api.us-east-1.amazonaws.com/dev/LambdaClima/crea"

url = "https://sddhex0a2j.execute-api.us-east-1.amazonaws.com/dev/LambdaClima/crea"

payload= '{\r\n    \"ciudad\":\"'+ciudad+'\"\r\n    }'


#payload="{\r\n    \"ciudad\":\"cordoba\"\r\n    }"

#print(pay)

headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)

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