# DjangoDemo

## Crear instancia de Django
1. Instalar Django mediante PIP `$ pip install django-admin`
2. Abrir el directorio donde se encuentra el proyecto de Django, el nivel del directorio debe ser el mismo de donde se encuentra el archivo manage.py
3. Ejecutar el servidor `$ python manage.py runserver`

## Instalacion de MongoDB
1. Descargar MongoDB Community Edition
2. Descargar MongoDB Compass
3. En la instalación del Community Edition Instalar como servicio
4. Verificar ingresando a localhost:27017

## Escribir BD Relacional
1. Crear modelo
2. Hacer migraciones con `$ python3 manage.py makemigrations`
3. Migrar los cambios a la base de datos con `$ python3 manage.py migrate`
4. Crear forma
5. Llamar a la clase de la forma
6. Esperar una respuesta POST
7. Validar el formulario con los datos introducidos
8. Verificar que el ID no este duplicado
9. Crear registro en la tabla
10. Desplegar mensaje

## Escribir BD No Relacional

1. Crear el formulario
2. Llamar a la clase del formulario
3. Esperar una respuesta POST
4. Validar el formulario con los datos introducidos
5. Verificar que el ID no este duplicado
6. Insertar el dato en la colección y con el nombre del documento correspondiente (JSON ObjectID)
7. Desplegar el mensaje correspondiente

## Leer BD Relacional

1. Hacer html y configuración de URLs
2. Llamar la función, obtener los datos en la base de datos con *get()*, *all()*, *filter()* y pasa los datos a la plantilla:
    -**get():** obtener un único registro que cumpla con las condiciones especificadas.

    -**all():** obtener todos los registros de una tabla.

    -**filter():** obtener un conjunto de registros que cumplan con las condiciones especificadas.

3. Pasar los datos a la html para mostrarlo


## Leer BD NO Relacional

1. conectar base de datos mongo
2. Hacer html y configuración de URLs
3. Llamar la función (obtener los datos en MongoDB con *find()* y pasa los datos usuarios a la plantilla):

    -**find_one():** recuperar un único documento que cumpla con los criterios de búsqueda especificados.

    -**find():** realizar consultas y recuperar documentos de una colección. (sin poner condición obtiene todos los registro de una colección)

4. Pasar los datos a la html para mostrarlo

