from typing import List
from django import views
from autenticacao.views import *
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from postagem.views import PostUsuarioViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/usuarios/',ListaUsuarioViewSet.as_view()),
    path('api/cadastro/',UsuarioCadastroViewSet.as_view()),
    path('api/usuario/post/',PostUsuarioViewSet.as_view()),
    path('api/login/',LogaUsuarioViewSet.as_view()),
    path('api/logout/', Logout.as_view()),
]