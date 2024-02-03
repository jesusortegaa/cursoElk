#La idea es simular una transaccion entre dos usuarios
import string
import random
import datetime

def crear_usuario():
    #Un usuario serán 3 letras y 6 numero
    user = ""
    ip = crear_ip()

    for i in range(3):
        user += random.choice(string.ascii_lowercase)
    for i in range(6):
        user += str(random.randint(0,9))
    
    objeto = {
        "user" : user,
        "ip" : ip
    }
    return objeto

def crear_usuarios(a):
    usuarios = []
    for i in range(a):
        usuarios.append(crear_usuario())
    return usuarios

def crear_ip():
    #255.255.255.255
    ip = ""
    for i in range(4):
        ip += str(random.randint(0,255))
        if(i<3):
            ip +="."
    return ip

def crear_os():
    #iOS, Android, Windows, Linux, macOS
    list = ["iOS", "Android", "Windows", "Linux", "macOS"]
    return random.choice(list)

def crear_accion():
    acciones = ["[SUCCESS] La transaccion se ha realizado correctamente",
                "[SUCCESS] La transaccion se ha realizado correctamente",
                "[SUCCESS] La transaccion se ha realizado correctamente",
                "[WARN] La transaccion ha tardado mas de lo esperado.",
                "[ERROR] La transaccion no se ha completado."]


    accion = random.choice(acciones).split(" ")
    loglevel = accion[0]
    resultado = " ".join(accion[1:])

    return loglevel, resultado

def crear_terminal():
    coord1 = (43.291944, -7.440000)
    coord2 = (37.318544, -5.272116)
    coord3 = (42.436934, -5.956972)
    coord4 = (40.079843, -0.620766)

    latitud_min = min(coord1[0], coord2[0], coord3[0], coord4[0])
    latitud_max = max(coord1[0], coord2[0], coord3[0], coord4[0])
    longitud_min = min(coord1[1], coord2[1], coord3[1], coord4[1])
    longitud_max = max(coord1[1], coord2[1], coord3[1], coord4[1])
    
    latitud_aleatoria = random.uniform(latitud_min, latitud_max)
    longitud_aleatoria = random.uniform(longitud_min, longitud_max)
    
    terminal = {"lat":latitud_aleatoria, "lon":longitud_aleatoria}
    return terminal

def crear_transaccion(usuario1, usuario2):
    terminal = crear_terminal()
    transaccion = {
        "source":usuario1["user"],
        "target":usuario2["user"],
        "amount": random.randint(1, 200),
        "terminal":terminal
    }

    return transaccion

def crear_fecha(actual):
    if(actual == False):
        inicio = datetime.datetime(2023, 1, 1)
        final = datetime.datetime(2024, 1, 1)
    else:
        inicio = datetime.datetime(2024, 1, 1)
        final = datetime.datetime(2024, 2, 12)
    
    random_date = inicio + (final - inicio) * random.random()
    return random_date

def crear_traza(usuarios, actual):
    usuario1 = random.choice(usuarios)
    usuario2 = random.choice(usuarios)
    user = usuario1["user"]
    ip = usuario1["ip"]
    os = crear_os()
    loglevel, action = crear_accion()
    fecha = crear_fecha(actual)
    transaction = crear_transaccion(usuario1,usuario2)

    traza = {
        "loglevel": loglevel,
        "user":user,
        "ip":ip,
        "os":os,
        "action" : action,
        "transaction":transaction,
        "date":str(fecha)
    }

    return traza

def get_mapping():
    # Mapeo de los campos de tu documento JSON
    mapping = {
        "mappings": {
            "properties": {
                "loglevel": {"type": "keyword"},
                "user": {"type": "keyword"},
                "ip": {"type": "ip"},
                "os": {"type": "keyword"},
                "action": {"type": "text"},
                "transaction": {
                    "properties": {
                        "source": {"type": "keyword"},
                        "target": {"type": "keyword"},
                        "amount": {"type": "integer"},
                        "terminal": {"type": "geo_point"}
                    }
                },
                "date": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"}
            }
        }
    }

    return mapping