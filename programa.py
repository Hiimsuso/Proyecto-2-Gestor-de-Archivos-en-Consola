import funciones as fc
import os


opcion = ""


while(opcion != 7):
  fc.mostrar_menu()
  try:
    opcion = int(input("Introduce una opción: "))
  except ValueError:
    print("Debes introducir un número")
    continue

  if opcion == 1:
    for i in fc.listar_contenido():
      if os.path.isfile(i):
        print(f"Archivo: {i}")
      elif os.path.isdir(i):
        print(f"Carpeta: {i}")

  elif opcion == 2:
    fc.crear_directorio()

  elif opcion == 3:
    fc.crear_archivo()

  elif opcion == 4:
    fc.escribir_en_archivo()

  elif opcion == 5:
    fc.eliminar_elemento()

  elif opcion == 6:
      fc.mostrar_informacion()

  elif opcion == 7:
      break

  else:
    print("Introduce un valor entre 1 y 7")
