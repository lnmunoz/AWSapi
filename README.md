# AWSapi

Dependencias necesarias:


Instalación de Serverless:

curl -o- -L https://slss.io/install | bash

En el presente directorio, se deberá ejecutar el siguiente comando:

serverless create --template aws-python3

Se deberán configurar los datos de accesos a AWS

serverless config credentials --provider aws --key "personalKey" --secret "personalSecret" --overwrite

Ademas, se deberá configurar el rol dentro de serverless.yml

Ejemplo:   role: arn:aws:iam::ID:role/ServRoleName

El despliegue se realizará con las siguiente orden:

serverless deploy

El resultado que devolverá contendrá el link de acceso a la API, este se deberá agregar al codigo de la app LambdaClima.py

Este se ejecuta: python3 LambdaClima.py
