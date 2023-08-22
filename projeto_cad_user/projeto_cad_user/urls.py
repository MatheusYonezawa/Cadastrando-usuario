
from django.urls import path
from app_cad_user import views

urlpatterns = [
    # rota, view responsável, nome de referencia
    # usuarios.com
    path('',views.index,name='index'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios, name='listagem_usuarios'),
]
