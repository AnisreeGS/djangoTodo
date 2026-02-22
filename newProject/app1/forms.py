from .models import Todo
from django import forms
from django.forms import TextInput

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_text']
        widgets = { 'todo_text':forms.TextInput(attrs={'type':"text", 
                                                       'class':"form-control", 
                                                       'placeholder':"Add your new todo"
                                                       }
                                                       )
                                                       }
        