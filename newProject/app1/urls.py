from django.urls import path
from . import views

urlpatterns = [
    path('', views.createTodo, name='createTodo'),  # ✅ no slash
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:task_id>/', views.deleteTodo, name='deleteTodo'),
    path('editTodo/<int:task_id>/', views.editTodo, name='editTodo'),
]
