from apptodolist.views import TodoListCreate, TodoDetailChangeDelete

from django.urls import path

urlpatterns = [
    path('', TodoListCreate.as_view()),
    path('<int:pk>/',TodoDetailChangeDelete.as_view()),
]