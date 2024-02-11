import json
from generador_logs import crear_traza, crear_usuarios

def crear_logs_fichero(numUsuarios, numTrazas):
    usuarios = crear_usuarios(numUsuarios)
    trazas = []
    for i in range(numTrazas):
        trazas.append(crear_traza(usuarios, False))

    with open("logstash/var/json.log", "w") as fichero:
        for i in range(numTrazas):
            fichero.write(json.dumps(trazas[i]))
            if(i!=numTrazas-1):
                fichero.write("\n")

    print("Se ha creado el fichero con trazas")

crear_logs_fichero(10, 10)