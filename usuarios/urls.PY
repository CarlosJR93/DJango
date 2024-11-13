from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal (inicio)
    path('ingresar/', views.ingresar, name='ingresar'),  # Página de ingresar
    path('lista/', views.lista, name='lista'),  # Lista de usuarios
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),  # Eliminar usuario
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
]
