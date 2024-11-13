from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('tasks/',  views.tasks, name='tasks'),
    path('tasksCompleted/',  views.tasksCompleted, name='tasksCompleted'),
    path('tasks/create/', views.createTask, name='createTask'),
    path('tasks/<int:task_id>/', views.taskDetails, name='taskDetails'),
    path('tasks/<int:task_id>/complete/',
         views.completeTask, name='completeTask'),
    path('tasks/<int:task_id>/delete/', views.deleteTask, name='deleteTask')
]
