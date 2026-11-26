import funciones as fc
import os
from colorama import Fore, Style

def main():
  opcion = ""

  while(opcion != 7):
    fc.mostrar_menu()
    try:
      opcion = int(input(f"{Fore.YELLOW}Introduce una opción: {Style.RESET_ALL}"))
    except ValueError:
      print(f"{Fore.RED}Debes introducir un número{Style.RESET_ALL}")
      continue

    if opcion == 1:
      for i in fc.listar_contenido():
        if os.path.isfile(i):
          print(f"{Fore.BLUE}Archivo: {i}{Style.RESET_ALL}")
        elif os.path.isdir(i):
          print(f"{Fore.YELLOW}Carpeta: {i}{Style.RESET_ALL}")

    elif opcion == 2:
      nombre = input(f"{Fore.YELLOW}introduce el nombre de la carpeta: {Style.RESET_ALL}")

      valor = fc.crear_directorio(nombre)
      if valor:
        print(f"{Fore.GREEN}Directorio {nombre} creado correctamente{Style.RESET_ALL}")
      else:
        print(f"{Fore.RED}El directorio ya existe{Style.RESET_ALL}")


    elif opcion == 3:
      nombre = input(f"{Fore.YELLOW}introduce el nombre del archivo: {Style.RESET_ALL}")
      contenido = input(f"{Fore.YELLOW}Indica que quieres escribir en el archivo: {Style.RESET_ALL}")
      valor = fc.crear_archivo(nombre, contenido)
      if valor:
        print(f"{Fore.GREEN}Archivo {nombre} creado correctamente{Style.RESET_ALL}")
      else:
        print(f"{Fore.RED}El archivo ya existe{Style.RESET_ALL}")

    elif opcion == 4:
      archivo = input(f"{Fore.YELLOW}Introduce el archivo sobre el que quieres escribir: {Style.RESET_ALL}")
      datos = input(f"{Fore.YELLOW}Introduce la información que deseas guardar: {Style.RESET_ALL}")

      valor = fc.escribir_en_archivo(archivo, datos)

      if valor:
        print(f"{Fore.GREEN}Información guardada correctamente{Style.RESET_ALL}")
      else:
        print(f"{Fore.RED}Debes introducir un nombre correcto de archivo{Style.RESET_ALL}")

    elif opcion == 5:
      archivo = input(f"{Fore.YELLOW}Introduce el archivo que deseas eliminar: {Style.RESET_ALL}")
      valor = fc.eliminar_elemento(archivo)
      print(valor)

    elif opcion == 6:
      nombre = input(f"{Fore.YELLOW}Introduce el nombre del archivo o carpeta: {Style.RESET_ALL}")
      valor = fc.mostrar_informacion(nombre)
      if valor:
        print(valor)
      else:
        print(f"{Fore.RED}El nombre indicado es incorrecto o no existe{Style.RESET_ALL}")

    elif opcion == 7:
      break

    else:
      print(f"{Fore.RED}Introduce un valor entre 1 y 7{Style.RESET_ALL}")

if __name__ == "__main__":
  main()
