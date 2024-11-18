from django.urls import path
from . import views

urlpatterns = [
    path('utiles/', views.inicioUtiles, name='inicioUtiles'),
]