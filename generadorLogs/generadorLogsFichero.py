import json
from generadorLogs import crearTraza, crearUsuarios

def crearLogFichero(usuarios, numTrazas):
    trazas = []
    for i in range(numTrazas):
        trazas.append(crearTraza(usuarios, False))
    
    with open("logs2Python.json", "a") as fichero:
        json.dump(trazas, fichero, indent=4)
    print("Se ha creado el fichero con trazas")

usuarios = crearUsuarios(10)
crearLogFichero(usuarios, 100)