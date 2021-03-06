from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import TaskSerializer
from tasks.models import Task

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/taskList/',
        'Detail View': '/taskDetail/<str:pk>/',
        'Create': '/taskCreate/',
        'Update': '/taskUpdate/<str:pk>/',
        'Delete': '/taskDelete/<str:pk>/',

    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)           


@api_view(['POST','GET'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("item succsesfully deleted!")                                 