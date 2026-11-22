import os
from datetime import datetime
from colorama import Fore, Style

def mostrar_menu():
    print(f"""
        {Fore.CYAN}=== GESTOR DE ARCHIVOS ===

        Ruta actual: {os.getcwd()}

        1. Listar archivos y carpetas
        2. Crear una carpeta
        3. Crear un archivo de texto
        4. Escribir en un archivo
        5. Eliminar un archivo o carpeta
        6. Mostrar información
        7. Salir
      {Style.RESET_ALL}""")

def listar_contenido():
    return os.listdir()

def crear_directorio(nombre):
    try:
      os.mkdir(nombre)
      return True
    except FileExistsError:
      return False

def crear_archivo(nombre, contenido):
    try:
      with open(nombre, "x", encoding='utf-8') as archivo:
          archivo.write(contenido)
      return True
    except FileExistsError:
      return False

def escribir_en_archivo(archivo, datos):
    if os.path.isfile(archivo):
        with open(archivo, "a", encoding="utf-8") as documento:
            documento.write(f"\n{datos}")
        return True
    else:
        return False


def eliminar_elemento(archivo):
  try:
    if os.path.isdir(archivo):
      os.rmdir(archivo)
      return f"{Fore.GREEN}El directorio {archivo} ha sido eliminado correctamente{Style.RESET_ALL}"
    elif os.path.isfile(archivo):
      os.remove(archivo)
      return f"{Fore.GREEN}El archivo {archivo} ha sido eliminado correctamente{Style.RESET_ALL}"
    else:
      return f"{Fore.RED}El archivo/carpeta indicado no existe{Style.RESET_ALL}"
  except OSError:
    return f"{Fore.RED}No se ha podido eliminar el archivo o directorio indicado{Style.RESET_ALL}"

def mostrar_informacion(nombre):
    if os.path.isfile(nombre):
      tipo = "Archivo"
    elif os.path.isdir(nombre):
      tipo = "Directorio"
    else:
       return False

    tamanio = os.path.getsize(nombre)
    tiempo = os.path.getmtime(nombre)
    fecha = datetime.fromtimestamp(tiempo)
    return f"""
    Nombre: {nombre}
    Tipo: {tipo}
    Tamaño: {tamanio}
    Última modificación: {fecha.strftime("%d/%m/%Y")}

    """


