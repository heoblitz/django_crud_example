from django.urls import include, path
from . import views

app_name = 'todo_main'

urlpatterns = [
    path(r'', views.Todo_main.as_view(), name='Todo_main'),
    path(r'insert/', views.check_post, name="Todo_main_insert")
]
