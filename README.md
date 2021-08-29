# CRUD backend

## Consulta Swagger

    NO se implementó swagger

## Crear todo en ambiente de Desarrollo

    Tener instalado Python 3
    Crear el entorno: 
        - python3 -m venv env
    Activar entorno: 
        - source env/bin/activate
    Instalar lo requerimientos de la aplicación
        - pip install -r requirements.txt 

## Correr pruebas unitarias

    - python manage.py test api.tests.PostUsuarioTest
    - python manage.py test api.tests.GetUsuarioListTest
    - python manage.py test api.tests.GetUsuarioDetailTest
    - python manage.py test api.tests.PutUsuarioTest
    - python manage.py test api.tests.DeleteUsuarioTest



## Notas:
    - Se incluye archivo sqlite, no es necesario hacer migraciones a la DB