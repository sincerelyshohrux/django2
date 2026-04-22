from django.urls import path
from . import views

# URL patterns for tasks app
urlpatterns = [
    path('', views.task_list, name='task_list'),           # List all tasks
    path('task/new/', views.task_create, name='task_create'),  # Create task
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # View task
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),  # Update task
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Delete task
]
