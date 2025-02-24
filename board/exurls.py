from . import views
from django.urls import path

app_name ="board"
urlpatterns =[
    path("", views.list.as_view(), name="list"),
    path("detail/<int:pk>/", views.detail.as_view(), name="detail"),
    path("create/",views.create.as_view(), name="create"),
    path("edit/<int:pk>/",views.edit.as_view(), name="edit"),
    path("delete/<int:pk>/",views.delete.as_view(), name="delete"),
]
