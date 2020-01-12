from django.shortcuts import render
from django.views import generic
# Create your views here.
from .forms import TodoForm # form 추가
from .models import Todo_list # model 추가

class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        todo_list = Todo_list.objects.all()

        return render(request, template_name, {"todo_list": todo_list})

class Todo_main_detail(generic.DetailView):
    model = Todo_list
    template_name = 'todo_main/todo_main_detail.html'
    context_object_name = 'todo_list'

    

def check_post(request):
    template_name = 'todo_main/todo_main_success.html'

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = '일정을 추가하였습니다.'

            return render(request, template_name, {"message": message})
        
    else:
        template_name = 'todo_main/todo_main_insert.html'
        form = TodoForm

        return render(request, template_name, {"form": form})
        