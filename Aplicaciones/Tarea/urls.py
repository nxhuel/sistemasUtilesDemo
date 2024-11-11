from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',  views.tasks, name='tasks'),
    path('home/', views.home, name='home'),
    path('tasks/create/', views.createTask, name='createTask'),
    path('tasks/<int:task_id>/', views.taskDetails, name='taskDetails')
]