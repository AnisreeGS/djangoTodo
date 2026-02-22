from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def createTodo(request):
    # return HttpResponse("Hello this is anisree from app1")
    forms = TodoForms()
    todo = Todo.objects.all()
    todo_details = {
        "tasks": todo,
        "forms" :forms
    }
    
    if request.method == "POST":
        forms = TodoForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('createTodo')
        
    return render(request,"index.html",todo_details)
@login_required
def deleteTodo(request,task_id):
    todo_dlt = Todo.objects.get(id=task_id)
    todo_dlt.delete()
    return redirect('createTodo')

# def clickEditIcon(request,task_id):
#     return redirect("edit.html")

# def editTodo(request,task_id):
#     todo_edt = Todo.objects.get(id=task_id)
#     if request.method == "POST":
#         # todo_edt.todo_text = request.POST.get("todo_text")
#         todo_edt= request.POST.get("todo_text")
#         edit_obj = TodoForms(todo_edt=todo_edt)
#         edit_obj.save()
#         return redirect('createTodo')
#     return render(request,"edit.html")

@login_required
def editTodo(request, task_id):
    # todo = Todo.objects.get(Todo,id=task_id)
    todo = get_object_or_404(Todo, id=task_id)
    print("Fetched:", todo.todo_text)
    if request.method == "POST":
        form = TodoForms(request.POST, instance=todo)
        print("Request Method:", request.method)
        if form.is_valid():
            form.save()
            return redirect('createTodo')
    else:
        form = TodoForms(instance=todo)

    return render(request, "edit.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('createTodo')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
