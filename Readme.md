# Verificación de Permisos de Archivos

Este script en Python permite verificar los permisos de un archivo en el sistema, mostrando los permisos en formato octal (por ejemplo, `755`, `644`). Es útil para asegurarse de que los archivos en tu sistema tengan los permisos adecuados y que se puedan manipular de forma segura.

## Funcionamiento

El código verifica si el archivo especificado por el usuario existe en el sistema. Si el archivo existe, extrae y muestra sus permisos en formato octal. Si el archivo no se encuentra, se informa al usuario con un mensaje claro de que el archivo no existe.

El proceso consta de los siguientes pasos:

1. **Verificación de existencia**: Se utiliza la función `os.path.exists()` para determinar si el archivo existe en el sistema.
2. **Obtención de permisos**: Si el archivo existe, se emplea `os.stat()` para obtener la información del archivo, y luego se convierte a un formato octal mediante `oct()`, extrayendo los últimos tres dígitos que representan los permisos del archivo.
3. **Salida de información**: Se imprime en consola el nombre del archivo junto con sus permisos o un mensaje que indica que el archivo no existe.

### Ejemplo de uso

Supongamos que tienes un archivo llamado `datos.csv` en tu sistema, puedes ejecutar el script de la siguiente manera:

```
Introduce el nombre del archivo: datos.csv
Permisos del archivo 'datos.csv': 644
```

Este resultado indica que el archivo `datos.csv` tiene permisos de lectura y escritura para el propietario, y solo de lectura para el grupo y otros.

Si el archivo no existe, el script responderá:

```
Introduce el nombre del archivo: datos.csv
El archivo 'datos.csv' no existe.
```

## **Utilidad en Ingeniería de Datos (Data Engineering)**

**Este código puede ser extremadamente útil en ingeniería de datos, donde es fundamental gestionar correctamente los permisos de los archivos y datos almacenados en diferentes sistemas.** Por ejemplo, al trabajar con archivos CSV, JSON u otros formatos en pipelines de datos, es crucial asegurarse de que los permisos sean correctos para garantizar la seguridad y accesibilidad adecuada a los datos. Verificar los permisos también ayuda a prevenir errores de lectura/escritura cuando los scripts automatizados manipulan grandes volúmenes de datos en proyectos de ETL (Extracción, Transformación y Carga).

## Consideraciones

- Asegúrate de que los archivos para los que deseas verificar los permisos existan en la ruta indicada, de lo contrario, recibirás un mensaje de que el archivo no fue encontrado.
- El formato de los permisos sigue el estándar UNIX, donde cada dígito representa los permisos del propietario, el grupo y otros usuarios, respectivamente.
- Este script es compatible solo con sistemas que utilicen permisos de archivos en formato octal, como Linux y macOS.

