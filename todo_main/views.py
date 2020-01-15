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

class Todo_main_update(generic.UpdateView):
    model = Todo_list
    fields = ('title', 'content', 'date')
    template_name = 'todo_main/todo_main_update.html'
    success_url = '/home/'

    def form_vaild(self, form):
        form.save()
        return render(self.request, 'todo_main/todo_main_success.html', {"message": "일정을 업데이트 했습니다"})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

class Todo_main_delete(generic.DeleteView):
    model = Todo_list
    template_name = 'todo_main/todo_main_delete.html'
    success_url = '/home/'

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
        