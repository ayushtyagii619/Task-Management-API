from django.urls import path, include
from .views import RegisterApiView, LoginApiView, CreateTaskApiView, TaskListApiView, TaskListByIdApiView, TaskUpdateApiView, TaskDeleteApiView
urlpatterns = [
    path('auth/register/',RegisterApiView.as_view(),name='register'),
    path('auth/login/',LoginApiView.as_view(),name='login'),
    path('tasks/create/',CreateTaskApiView.as_view(),name='create-task'),
    path('tasks/',TaskListApiView.as_view(),name='tasks-list'),
    path('tasks/<int:id>/',TaskListByIdApiView.as_view(),name='list-id-tasks'),
    path('tasks/update/<int:id>/',TaskUpdateApiView.as_view(),name='task-update'),
    path('tasks/delete/<int:id>/',TaskDeleteApiView.as_view(),name='task-delete')
]