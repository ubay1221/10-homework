from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('list/', views.task_list, name='list'),
    path('create/', views.create_task, name='create'),
    path('detail/<int:task_id>', views.task_detail, name='detail'),
    path('delete/<int:task_id>', views.task_delete, name='delete'),
    path('update/<int:task_id>', views.task_update, name='update'),
]