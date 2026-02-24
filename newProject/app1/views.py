from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.


@login_required
def createTodo(request):
    # return HttpResponse("Hello this is anisree from app1")
    forms = TodoForms()
    todo = Todo.objects.all()
    # todo_details = {
    #     "tasks": todo,
    #     "forms" :forms
    # }
    
    if request.method == "POST":
        forms = TodoForms(request.POST)
        if forms.is_valid():
            todo = forms.save(commit=False)  # Create a Todo instance without saving to the database yet
            todo.user = request.user
            forms.save()
            return redirect('createTodo')
    todo_details = Todo.objects.filter(user=request.user)

    form = TodoForms()
    return render(request,"index.html",{"tasks": todo_details, "forms": form})

@login_required
def deleteTodo(request,task_id):
    # todo_dlt = Todo.objects.get(id=task_id)
    todo_dlt = get_object_or_404(Todo, id=task_id, user=request.user)
    todo_dlt.delete()
    return redirect('createTodo')



@login_required
def editTodo(request, task_id):
    # todo = Todo.objects.get(Todo,id=task_id)
    todo = get_object_or_404(Todo, id=task_id, user=request.user)
    # todo = get_object_or_404(Todo, id=task_id)
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

def registeruser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')

    return render(request, 'registeruser.html')