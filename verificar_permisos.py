import os

# Verifica si el archivo existe y muestra los permisos
def verificar_permisos(archivo):
    if os.path.exists(archivo):
        permisos = oct(os.stat(archivo).st_mode)[-3:]
        print(f"Permisos del archivo '{archivo}': {permisos}")
    else:
        print(f"El archivo '{archivo}' no existe.")

# Ejemplo de uso
archivo = input("Introduce el nombre del archivo: ")
verificar_permisos(archivo)
