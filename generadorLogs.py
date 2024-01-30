#La idea es simular una transaccion entre dos usuarios

import string
import random
import time
import datetime

def crearUsuario():
    #Un usuario serán 3 letras y 6 numero
    user = ""
    ip = crearIp()

    for i in range(3):
        user += random.choice(string.ascii_lowercase)
    for i in range(6):
        user += str(random.randint(0,9))
    
    objeto = {
        "user" : user,
        "ip" : ip
    }
    return objeto

def crearUsuarios(a):
    usuarios = []
    for i in range(a):
        usuarios.append(crearUsuario())
    return usuarios

def crearIp():
    #255.255.255.255
    ip = ""
    for i in range(4):
        ip += str(random.randint(0,255))
        if(i<3):
            ip +="."
    return ip

def crearOS():
    #iOS, Android, Windows, Linux, macOS
    list = ["iOS", "Android", "Windows", "Linux", "macOS"]
    return random.choice(list)

def crearAccion():
    acciones = ["[SUCCESS] La transaccion se ha realizado correctamente",
                "[SUCCESS] La transaccion se ha realizado correctamente",
                "[SUCCESS] La transaccion se ha realizado correctamente",
                "[WARN] La transaccion ha tardado mas de lo esperado.",
                "[ERROR] La transaccion no se ha completado."]


    accion = random.choice(acciones).split(" ")
    loglevel = accion[0]
    resultado = " ".join(accion[1:])

    return loglevel, resultado


def crearTerminal():
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
    
    return (latitud_aleatoria, longitud_aleatoria)

def crearTransaccion(usuario1, usuario2):
    terminal = crearTerminal()
    transaccion = {
        "source":usuario1["user"],
        "target":usuario2["user"],
        "amount": random.randint(1, 200),
        "terminal":terminal
    }

    return transaccion

def crearFecha(actual):
    if(actual == False):
        inicio = datetime.datetime(2023, 1, 1)
        final = datetime.datetime(2024, 1, 1)
    else:
        inicio = datetime.datetime(2024, 1, 1)
        final = datetime.datetime(2024, 2, 12)
    
    random_date = inicio + (final - inicio) * random.random()
    return random_date

def crearLogInicial(usuarios):
    for i in range(1, 10):
        usuario1 = random.choice(usuarios)
        usuario2 = random.choice(usuarios)
        user = usuario1["user"]
        ip = usuario1["ip"]
        os = crearOS()
        loglevel, action = crearAccion()
        fecha = crearFecha(False)
        transaction = crearTransaccion(usuario1,usuario2)
        
        objeto = {
            "loglevel": loglevel,
            "user":user,
            "ip":ip,
            "os":os,
            "action" : action,
            "transaction":transaction,
            "date":str(fecha)
        }
        with open("logsPython.log","a") as fichero:
            fichero.write(str(objeto).replace("'", "\"")+"\n")

def crearLogTiempoReal(usuarios):
    while(True):
        usuario1 = random.choice(usuarios)
        usuario2 = random.choice(usuarios)
        user = usuario1["user"]
        ip = usuario1["ip"]
        os = crearOS()
        loglevel, action = crearAccion() 
        fecha = crearFecha(True)
        transaction = crearTransaccion(usuario1,usuario2)
    
        objeto = {
            "loglevel": loglevel,
            "user":user,
            "ip":ip,
            "os":os,
            "action" : action,
            "transaction":transaction,
            "date":str(fecha)
        }
        
        time.sleep(1)
        with open("logsPython.log","a") as fichero:
            fichero.write(str(objeto).replace("'", "\"")+"\n")

usuarios = crearUsuarios(10)

crearLogInicial(usuarios)
crearLogTiempoReal(usuarios)