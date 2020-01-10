from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.Todo_main.as_view(), name='Todo_main')
]
