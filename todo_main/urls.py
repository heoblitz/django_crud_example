from django.urls import include, path
from . import views

app_name = 'todo_main'

urlpatterns = [
    path('', views.Todo_main.as_view(), name='Todo_main'),
    path('insert/', views.check_post, name="Todo_main_insert"),
    path('<int:pk>/detail/', views.Todo_main_detail.as_view(), name="Todo_main_detail"),
    path('<int:pk>/update/', views.Todo_main_update.as_view(), name="Todo_main_update"),
    path('update_save/', views.Todo_main_update.form_vaild, name="Todo_main_update_save"),
]
