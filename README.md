# DjangoDemo

##Crear instancia de Django
Instalar Django mediante PIP `$ pip install django-admin`

Abrir el directorio donde se encuentra el proyecto de Django, el nivel del directorio debe ser el mismo de donde se encuentra el archivo manage.py
Ejecutar el servidor `$ python manage.py runserver`

##Instalacion de MongoDB
Descargar MongoDB Community Edition
Descargar MongoDB Compass
En la instalación del Community Edition Instalar como servicio
Verificar ingresando a localhost:27017

##Escribir BD Relacional
Crear modelo
Hacer migraciones con `$ python3 manage.py makemigrations`
Migrar los cambios a la base de datos con `$ python3 manage.py migrate`
Crear forma
Llamar a la clase de la forma
Esperar una respuesta POST
Validar el formulario con los datos introducidos
Verificar que el ID no este duplicado
Crear registro en la tabla
Desplegar mensaje

##Escribir BD No Relacional

Crear el formulario
Llamar a la clase del formulario
Esperar una respuesta POST
Validar el formulario con los datos introducidos
Verificar que el ID no este duplicado
Insertar el dato en la colección y con el nombre del documento correspondiente (JSON ObjectID)
Desplegar el mensaje correspondiente

##Leer BD Relacional

Hacer html y configuración de URLs
Llamar la función, obtener los datos en la base de datos con *get()*, *all()*, *filter()* y pasa los datos a la plantilla
**get():** obtener un único registro que cumpla con las condiciones especificadas. 
**all():** obtener todos los registros de una tabla.
**filter():** obtener un conjunto de registros que cumplan con las condiciones especificadas.
Pasar los datos a la html para mostrarlo


##Leer BD NO Relacional

conectar base de datos mongo
Hacer html y configuración de URLs
Llamar la función (obtener los datos en MongoDB con *find()* y pasa los datos usuarios a la plantilla)
**find_one():** recuperar un único documento que cumpla con los criterios de búsqueda especificados.
**find():** realizar consultas y recuperar documentos de una colección. (sin poner condición obtiene todos los registro de una colección)
Pasar los datos a la html para mostrarlo

