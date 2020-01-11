from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Todo_list # model 추가

class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        todo_list = Todo_list.objects.all()

        return render(request, template_name, {"todo_list": todo_list})