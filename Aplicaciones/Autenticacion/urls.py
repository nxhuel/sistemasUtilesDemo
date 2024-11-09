from django.urls import path
from . import views

urlpatterns = [
    path('', views.singup, name='signup')
]