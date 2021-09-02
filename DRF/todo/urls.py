from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.api, name="api-overview"),
    path("tasklist/", views.taskList, name="tasklist"),
    path("taskdetail/<str:pk>", views.taskDetail, name="taskdetail"),
    path("taskcreate/", views.taskCreate, name="taskcreate"),
    path("taskupdate/<str:pk>", views.taskUpdate, name="taskupdate"),
    path("taskdelete/<str:pk>", views.taskDelete, name="taskdelete"),
]
