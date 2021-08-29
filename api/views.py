from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView

from api.exceptions import *
from .serializers import *


# POST
class UsuarioCreateView(CreateAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            return self.create(request, *args, **kwargs)
        raise BadRequest(serializer.errors)


# GET LIST
class UsuarioListView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer


# GET DETAIL
class UsuarioDetailView(RetrieveAPIView):
    queryset = Usuario.objects.filter()
    serializer_class = UsuarioListSerializer


# PUT
class UsuarioUpdateView(UpdateAPIView):
    queryset = Usuario.objects.filter()
    serializer_class = UsuarioSerializer


# DELETE
class UsuarioDeleteView(DestroyAPIView):
    queryset = Usuario.objects.filter()
