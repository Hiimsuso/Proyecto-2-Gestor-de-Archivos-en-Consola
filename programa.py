import funciones
import os


opcion = ""


while(opcion != 7):
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

  opcion = int(input("Introduce una opción: "))

  if opcion == 1:
    for i in funciones.listar_contenido():
      if os.path.isfile(i):
        print(f"Archivo: {i}")
      elif os.path.isdir(i):
        print(f"Carpeta: {i}")

