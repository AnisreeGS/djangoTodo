from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoDisplay(admin.ModelAdmin):
    list_display = ['id','todo_text']