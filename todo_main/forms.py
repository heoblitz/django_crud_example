from django import forms
from .models import Todo_list

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_list
        fields = {'title', 'content', 'date', 'is_complete'}