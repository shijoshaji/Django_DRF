from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from . serializer import TaskSerializer
from .models import Task

#  import DRF related
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def api(request):
    api_urls = {
        'List': '/tasklist/',
        'Detail View': '/taskdetail/<str:pk>/',
        'Create': 'taskcreate/',
        'Update': 'task-update/<str:pk>/',
        'Delete': 'task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serialiser = TaskSerializer(tasks, many=True)

    return Response(serialiser.data)


@api_view(['GET'])
def taskDetail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serialiser = TaskSerializer(task, many=False)
        return Response(serialiser.data)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def taskCreate(request):
    serialiser = TaskSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data, status=status.HTTP_201_CREATED)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serialiser = TaskSerializer(instance=task, data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
