from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo
from todo.serializers import TodoSerializer


# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
