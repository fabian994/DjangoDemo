# DjangoDemo

Documentacion oficial de Django: https://docs.djangoproject.com/en/4.2/

## Crear instancia de Django
1. Instalar Django mediante PIP `$ pip install django-admin`
2. Abrir el directorio donde se encuentra el proyecto de Django, el nivel del directorio debe ser el mismo de donde se encuentra el archivo manage.py
3. Ejecutar el servidor `$ python manage.py runserver`

## Crear Aplicacion de Django

1. Crear App mediante `$ python manage.py startapp polls`
2. Añadir las aplicacion a settings.py, en la seccion de `INSTALLED_APPS`, usando el nombre de la aplicacion en comillas.
3. Crear archivo `urls.py` en el folder de la aplicacion
4. Dentro del archivo `urls.py` dentro de la carpeta del proyecto de Django, incluir el archivo `urls.py` de la aplicacion de la siguiente manera: `path('', include('appName.urls')),`
5. Dentro del folder de la app, crear carpetas `static` y `templates` donde se guardaran archivos de Js y Css, en el segundo se guardaran todos los archivos de HTML

## Instalacion de MongoDB
1. Descargar MongoDB Community Edition
2. Descargar MongoDB Compass
3. En la instalación del Community Edition Instalar como servicio
4. Verificar ingresando a localhost:27017

## Escribir BD Relacional
1. Crear modelo en el archivo `models.py` dentro del folder de la aplicacion
2. Hacer migraciones con `$ python3 manage.py makemigrations`
3. Migrar los cambios a la base de datos con `$ python3 manage.py migrate`
4. Crear archivo `forms.py` en el folder de la aplicacion y [crear forma](https://docs.djangoproject.com/en/4.2/topics/forms/) dentro del archivo.
5. Importar formas y modelos en el archivo `views.py` dentro del folder de la app.
6. [Crear views](https://docs.djangoproject.com/en/4.2/topics/http/views/) dentro del archivo `views.py`
5. Llamar a la clase de la forma
6. Esperar una respuesta POST
7. Validar el formulario con los datos introducidos
8. Verificar que el ID no este duplicado
9. Crear registro en la tabla usando el modelo atraves de `modelName.objects.create(data)`
10. Desplegar mensaje

## Escribir BD No Relacional
1. Instalar Pymongo `$ pip install pymongo`
1. Crear el formulario
2. Llamar a la clase del formulario
3. Esperar una respuesta POST
4. Validar el formulario con los datos introducidos
5. Verificar que el ID no este duplicado
6. Insertar el dato en la colección y con el nombre del documento correspondiente (JSON ObjectID) a traves de `db.collectionName.insert_one(dictionaryWithData)`
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

