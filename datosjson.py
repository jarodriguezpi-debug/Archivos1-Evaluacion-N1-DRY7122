import json

# Abrir el archivo y establecer la variable json_file
with open('myfile.json', 'r') as json_file:
    # Cargar el archivo en la variable ourjson
    ourjson = json.load(json_file)

# Imprimir el token y el tiempo de caducidad
print("Token:", ourjson.get("access_token"))
print("Tiempo restante antes de caducar:", ourjson.get("expires_in"), "segundos")
