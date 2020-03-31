from django.urls import path
from . import views

urlpatterns = [
    path ('api/', views.apiOverview, name='apiOverview'), 
    path ('taskList/', views.taskList, name="taskList"),
    path('taskDetail/<str:pk>/', views.taskDetail, name="taskDetail"),
    path ('taskCreate/', views.taskCreate, name="taskCreate"),
    path('taskUpdate/<str:pk>/', views.taskUpdate, name="taskUpdate"),
    path('taskDelete/<str:pk>/', views.taskDelete, name="taskDelete"),
]