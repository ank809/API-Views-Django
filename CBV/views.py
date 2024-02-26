from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
import json

class StudentViews(APIView):
    def get(self, request,pk, format=None):
        if pk is not None:
            try:
                stu=Student.objects.get(id=pk)
            except Student.DoesNotExist:
                return Response("does not exist", status=status.HTTP_404_NOT_FOUND)
            serializer=StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        # gives data in dictionary
        # data=request.data
        data = json.loads(request.body)
        print("Request Body:", request.body)
        if request.method=='POST':
            serializer=StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self, request,pk, format=None, ):
        try:
            stu=Student.objects.get(id=pk)
            stu.delete()
            return Response('deleted')
        except:
            return Response("not found", status=status.HTTP_204_NO_CONTENT)
        
    def put(self, request, pk,format=None):
        instance=Student.objects.get(id=pk)
        data = json.loads(request.body)
        serializer=StudentSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
