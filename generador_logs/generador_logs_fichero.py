import json
from generador_logs import crear_traza, crear_usuarios

def crear_logs_fichero(numUsuarios, numTrazas):
    usuarios = crear_usuarios(numUsuarios)
    trazas = []
    for i in range(numTrazas):
        trazas.append(crear_traza(usuarios, False))
    
    with open("logsTransacciones.json", "w") as fichero:
        json.dump(trazas, fichero, indent=4)
    print("Se ha creado el fichero con trazas")

#crearLogFichero(10, 100)
