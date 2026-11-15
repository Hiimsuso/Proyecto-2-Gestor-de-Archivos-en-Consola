import os
from datetime import datetime


def mostrar_menu():
    print(f"""
        === GESTOR DE ARCHIVOS ===

        Ruta actual: {os.getcwd()}

        1. Listar archivos y carpetas
        2. Crear una carpeta
        3. Crear un archivo de texto
        4. Escribir en un archivo
        5. Eliminar un archivo o carpeta
        6. Mostrar información
        7. Salir
      """)

def listar_contenido():
    return os.listdir()

def crear_directorio():
    try:
      nombre = input("introduce el nombre de la carpeta: ")
      os.mkdir(nombre)
    except FileExistsError:
        print("El directorio ya existe")

def crear_archivo():
    try:
      nombre = input("introduce el nombre del archivo: ")
      contenido = input("Indica que quieres escribir en el archivo: ")
      with open(nombre, "x", encoding='utf-8') as archivo:
          archivo.write(contenido)
    except FileExistsError:
        print("El archivo ya existe")

def escribir_en_archivo():
    archivo = input("Introduce el archivo sobre el que quieres escribir: ")
    if os.path.isfile(archivo) == False:
        print("Debes introducir un nombre correcto de archivo")
    else:
        datos = input("Introduce la información que deseas guardar: ")
        with open(archivo, "a", encoding="utf-8") as documento:
          documento.write(datos)


def eliminar_elemento():
    try:
      archivo = input("Introduce el archivo que deseas eliminar: ")
      if os.path.isdir(archivo):
          os.rmdir(archivo)
      elif os.path.isfile(archivo):
          os.remove(archivo)
      else:
          print("El archivo/carpeta indicado no existe")
    except OSError:
        print("No se ha podido eliminar el archivo o directorio indicado")

def mostrar_informacion():
    nombre = input("Introduce el nombre del archivo o carpeta: ")
    if os.path.isfile(nombre):
        tamanio = os.path.getsize(nombre)
        tiempo = os.path.getmtime(nombre)
        fecha = datetime.fromtimestamp(tiempo)
        print(f"""
        Nombre: {nombre}
        Tipo: Archivo
        Tamaño: {tamanio}
        Última modificación: {fecha.strftime("%d/%m/%Y")}

        """)
    elif os.path.isdir(nombre):
        tamanio = os.path.getsize(nombre)
        tiempo = os.path.getmtime(nombre)
        fecha = datetime.fromtimestamp(tiempo)
        print(f"""
        Nombre: {nombre}
        Tipo: Directorio
        Tamaño: {tamanio}
        Última modificación: {fecha.strftime("%d/%m/%Y")}
        """)
    else:
        print("El nombre del archivo/documento introducido no es correcto.")


def main():
    # Bucle principal del programa
    pass
