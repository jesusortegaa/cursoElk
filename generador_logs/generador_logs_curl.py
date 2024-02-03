import json
from time import sleep
import requests

from generador_logs import crear_traza, crear_usuarios, get_mapping

# Definir la URL de la solicitud
elasticsearch_url = "http://localhost:9200/"
#Definir el nombre del índice
index_name = "curso_kibana3"
# Definir URL para la indexación (usando API _doc)
url_indexacion = f"{elasticsearch_url}{index_name}/_doc"
#Definir el header de las peticiones HTTP (para establecer que le pasamos un JSON)
headers = {"Content-Type": "application/json"}
#Variable que almacena el mapeado de datos de la traza que se enviará a Elasticsearch
mapping = get_mapping()
#Definir los usuarios que apareceran en las trazas
usuarios = crear_usuarios(10)

def check_response(response):
    if response.status_code == 200:
        print("Solicitud exitosa")
        print(response.json())
    else:
        print("Error en la solicitud")
        print(response.status_code)
        print(response.json())
        print(response.text)

def eliminar_indice():
    #Eliminamos el índice si existe
    #DELETE /indice
    response = requests.delete(elasticsearch_url+index_name)
    check_response(response)

def crear_indice_con_mapping():
    # Creamos el índice y establecer el mapeado de los datos
    #PUT /indice
    response = requests.put(elasticsearch_url+index_name, json=mapping)
    check_response(response)

def indexar_sin_id():
    #Indexar documentos (sin ID)
    #POST /indice/_doc
    traza = json.dumps(crear_traza(usuarios, False))
    response = requests.post(url_indexacion, data=traza, headers=headers)
    check_response(response)

def indexar_con_id(id, actual):
    #Indexar documentos (con ID)
    #POST /indice/_doc/100 (por ejemplo)
    traza = json.dumps(crear_traza(usuarios, actual))
    url_indexacion_con_id = f"{elasticsearch_url}{index_name}/_doc/{id}"
    response = requests.post(url_indexacion_con_id, data=traza, headers=headers)
    check_response(response)

def get_document(id):
    #Recuperar documentos (con ID)
    #GET /indice/_doc/100
    traza = json.dumps(crear_traza(usuarios, False))
    url_get_con_id = f"{elasticsearch_url}{index_name}/_doc/{id}"
    response = requests.get(url_get_con_id, data=traza, headers=headers)
    check_response(response)

def enviarTrazaElastic(usuarios):
    i = 1
    while(True):
        indexar_con_id(i, True)
        i = i+1
        sleep(1)

crear_indice_con_mapping()
enviarTrazaElastic(usuarios)


