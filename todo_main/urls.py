from django.urls import include, path
from . import views

from django.

urlpatterns = [
    path(r'^$', views.Todo_main.as_view(), name='Todo_main')
]
