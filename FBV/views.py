from django.shortcuts import render
from rest_framework.decorators import api_view
from .models  import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
def getteacher(request):
        data=Teacher.objects.all()
        serializer=TeacherSerializer(data, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET'])
def getteacherbyid(request, pk):
    try:
        data=Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return Response("Teacher does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer=TeacherSerializer(data)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['POST'])
def addteacher(request):
     data=json.loads(request.body)
     serializer=TeacherSerializer(data=data)
     if serializer.is_valid():
          serializer.save()
          return Response('saved', status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatedata(request, pk):
    try:
        instance=Teacher.objects.get(id=pk)   
    except Teacher.DoesNotExist:
        return Response("Teacher does not exist", status=status.HTTP_404_NOT_FOUND)
    
    data=json.loads(request.body)
    serializer=TeacherSerializer(data=data, instance=instance, partial=True)
    if serializer.is_valid():
         serializer.save()
         return Response('saved', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteteacher(request, pk):
     try:
          teacher=Teacher.objects.get(id=pk)
     except Teacher.DoesNotExist:
          return Response("Teacher does not exist", status=status.HTTP_404_NOT_FOUND)
     teacher.delete()
     return Response("deleted", status=status.HTTP_200_OK)


