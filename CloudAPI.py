import requests
ciudad = input("Ingrese nombre de ciudad: ")

city = "https://v1.nocodeapi.com/lmunoz/ow/gypnqySHxLOMWguT/byCityName?q="+ciudad

print(city)
response = requests.get(city)
result = response.json()

#print(response.status_code) 
#print(result)

#"print( "En la ciudad de "+result.get("name")+" it is"+ str(result.get("temp"))+ "Chau" )


for key, value in result.items():
    print(key,':', value)


