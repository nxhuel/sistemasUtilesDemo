from django.urls import path
from . import views

urlpatterns = [
    path('intranet/', views.intranet, name='intranet'),
    path('aplicativos/', views.aplicativos, name='aplicativos')
]