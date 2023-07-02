from django.shortcuts import render
# from rest_framework.decorators import api_view # for function based api_view.
from rest_framework.response import Response
from .models import Student_model
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Crud in 3 lines below:
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student_model.objects.all()
#     serializer_class = StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student_model.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



# classBased api view is below:
"""
class Student_api(APIView):
    def get(self, request, pk=None, formate=None):
        uid = pk
        if uid is not None:
            stu = Student_model.objects.get(id=uid)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student_model.objects.all()
            serializer = StudentSerializer(stu, many = True)
            return Response(serializer.data)

    def post(self, request, formate=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data incerted Successfully"}, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, formate = None):
        uid = pk
        stu = Student_model.objects.get(id=uid)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User completely updated"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, formate = None):
        uid = pk
        stu = Student_model.objects.get(id=uid)
        serializer = StudentSerializer(stu,data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":" Partial User updated successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, formate = None):
        uid = pk
        stu = Student_model.objects.get(id =uid)
        stu.delete()
        return Response({'msg':'User deleted successfully'})
"""
