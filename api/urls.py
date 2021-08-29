from django.urls import path, re_path
from rest_auth import urls as urls_rest

from .views import *

app_name = 'api'

urlpatterns = [
    # POST
    path('usuario/create/', UsuarioCreateView.as_view(), ),
    # GET LIST
    path('usuario/list/', UsuarioListView.as_view(), ),
    # GET DETAIL
    path('usuario/<pk>/detail/', UsuarioDetailView.as_view(), ),
    # PUT
    path('usuario/<pk>/update/', UsuarioUpdateView.as_view(), ),
    # DELETE
    path('usuario/<pk>/delete/', UsuarioDeleteView.as_view(), ),

]
