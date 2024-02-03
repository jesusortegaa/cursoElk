import tkinter as tk
from generador_logs_fichero import crear_logs_fichero
from generador_logs import crear_usuarios
from generador_logs_curl import *


# Funciones para manejar eventos de botón
def clic_boton1():
    # Función que se ejecuta al hacer clic en el Botón 1
    ventana_secundaria = tk.Toplevel(ventana_principal)
    ventana_principal.withdraw()  # Oculta la ventana principal

    # Crear botones en la nueva ventana
    boton3 = tk.Button(ventana_secundaria, text="Indexar documento sin mapeado", command=indexar_sin_id())
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana_secundaria, text="Indexar documento con mapeado", command=indexar_con_id(100))
    boton4.pack(pady=10)

    boton5 = tk.Button(ventana_secundaria, text="Eliminar indice", command=eliminar_indice())
    boton5.pack(pady=10)

    boton6 = tk.Button(ventana_secundaria, text="Generar trazas en vivo")
    boton6.pack(pady=10)

    # Función para volver a la ventana principal
    def volver_a_principal():
        ventana_secundaria.destroy()  # Cierra la ventana secundaria
        ventana_principal.deiconify()  # Muestra la ventana principal nuevamente

    # Botón "Volver"
    boton_volver = tk.Button(ventana_secundaria, text="Volver", command=volver_a_principal)
    boton_volver.pack(pady=10)

def clic_boton2():
    crear_logs_fichero(10, 100)
    print("Se ha creado un nuevo fichero de logs")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")

usuarios = crear_usuarios(10)

# Definir el tamaño de la ventana principal (ancho x alto)
ventana_principal.geometry("400x300")

# Crear botones
boton1 = tk.Button(ventana_principal, text="API Elasticsearch", command=clic_boton1)
boton1.pack(pady=10)

boton2 = tk.Button(ventana_principal, text="Generar fichero de logs", command=clic_boton2)
boton2.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana_principal.mainloop()
