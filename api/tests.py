from .models import *

from rest_framework.test import APITestCase
import json
from rest_framework import status


def configDB():
    usuario1 = Usuario.objects.create(name='Gabriel Quiroz Olvera', email='gbrl.quiroz@gmail.com', password='gqo369')
    usuario2 = Usuario.objects.create(name='Fulanito Perez Lopez', email='usr2@usr2.com', password='asd222')
    usuario3 = Usuario.objects.create(name='Teofilita Sanchez Rodriguez', email='usr3@gusr3.com', password='asd333')

    ExtraInfo.objects.create(direccion='direccion1', telefono='tel1', fechaNacimiento='2001-01-01', usuario=usuario1)
    ExtraInfo.objects.create(direccion='direccion2', telefono='tel2', fechaNacimiento='2002-02-02', usuario=usuario2)
    ExtraInfo.objects.create(direccion='direccion3', telefono='tel3', fechaNacimiento='2003-11-11', usuario=usuario3)


# ----------------------------------------------------------------------------------- prueba unitaria del POST
# python manage.py test api.tests.PostUsuarioTest
class PostUsuarioTest(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "name": "user 4",
            "email": "usr_4@gusr4.com",
            "password": "asd444"
        }

        self.json2 = {
            "name": "user 5",
            "email": "usr_5@gusr5.com",
            "password": "asd555",
            "extraInfo": {
                "direccion": "direccion5",
                "telefono": "telefono5",
                "fechaNacimiento": "2000-05-05"
            }
        }

    def test(self):
        response = self.client.post('/api/usuario/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # nuevo registro deben ser 4
        self.assertEqual(4, Usuario.objects.count())

        response = self.client.post('/api/usuario/create/', data=json.dumps(self.json2), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # nuevo registro deben ser 5
        self.assertEqual(5, Usuario.objects.count())

        # solo se agrego un nuevo extraInfo deben ser 4 registros
        cuenta = ExtraInfo.objects.count()
        self.assertEqual(4, ExtraInfo.objects.count())


# ----------------------------------------------------------------------------------- prueba unitaria del GET LIST
# python manage.py test api.tests.GetUsuarioListTest
class GetUsuarioListTest(APITestCase):
    def setUp(self):
        configDB()

    def test(self):
        response = self.client.get('/api/usuario/list/')
        print(f'response JSON ===>>> all \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# ----------------------------------------------------------------------------------- prueba unitaria del GET DETAIL
# python manage.py test api.tests.GetUsuarioDetailTest
class GetUsuarioDetailTest(APITestCase):
    def setUp(self):
        configDB()

    def test(self):
        response = self.client.get('/api/usuario/3/detail/')
        print(f'response JSON ===>>> all \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# ----------------------------------------------------------------------------------- prueba unitaria del PUT
# python manage.py test api.tests.PutUsuarioTest
class PutUsuarioTest(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "name": "user X",
            "email": "usr_X@gusrX.com",
            "password": "asdXXX"
        }

        self.json2 = {
            "name": "user Y",
            "email": "usr_Y@gusrY.com",
            "password": "asdYYY",
            "extraInfo": {
                "direccion": "direccionY",
                "telefono": "telefonoY",
                "fechaNacimiento": "2000-06-06"
            }
        }

    def test(self):
        response = self.client.put('/api/usuario/1/update/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # registro modificado deben ser 3
        self.assertEqual(3, Usuario.objects.count())

        response = self.client.put('/api/usuario/3/update/', data=json.dumps(self.json2), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # registro modificado deben ser 3
        self.assertEqual(3, Usuario.objects.count())

        # no se agrego nada, deben ser 3 extra info
        cuenta = ExtraInfo.objects.count()
        self.assertEqual(3, ExtraInfo.objects.count())


# ----------------------------------------------------------------------------------- prueba unitaria del POST
# python manage.py test api.tests.DeleteUsuarioTest
class DeleteUsuarioTest(APITestCase):
    def setUp(self):
        configDB()

    def test(self):
        response = self.client.delete('/api/usuario/2/delete/')
        print(f'response JSON ===>>> ok 204 sin contenido \n {response.content} \n ---')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # solo deben existir 2 registros
        self.assertEqual(2, Usuario.objects.count())
        self.assertEqual(2, ExtraInfo.objects.count())
