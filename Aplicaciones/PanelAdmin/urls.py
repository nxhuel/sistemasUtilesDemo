from django.urls import path
from . import views

urlpatterns = [
    path('administracion/', views.administracion, name='administracion'),
    path('eliminarUsuario/<id>', views.eliminarUsuario),
    path('editarUsuario/<int:id>/', views.editarUsuario, name='editarUsuario'),
]