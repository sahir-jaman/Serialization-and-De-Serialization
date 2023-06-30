from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student_model
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def student_api(request, pk = None): # if the value is given the pk = value or pk = None
    if request.method == 'GET':
        uid = pk
        if uid is not None:
            stu = Student_model.objects.get(id=uid)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student_model.objects.all()
            serializer = StudentSerializer(stu, many = True)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data incerted Successfully"}, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        uid = pk
        stu = Student_model.objects.get(id=uid)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User completely updated"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        uid = pk
        stu = Student_model.objects.get(id=uid)
        serializer = StudentSerializer(stu,data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":" Partial User updated successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        uid = pk
        stu = Student_model.objects.get(id =uid)
        stu.delete()
        return Response({'msg':'User deleted successfully'})




