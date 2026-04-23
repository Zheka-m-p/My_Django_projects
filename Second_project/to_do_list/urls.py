from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # path('', views.to_do_home, name='to_do_home'),
    path('', views.TaskListView.as_view(), name='to_do_home'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task_create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task_update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),

    path('task/<int:pk>/toggle/', views.toggle_task, name='task_toggle'),

]