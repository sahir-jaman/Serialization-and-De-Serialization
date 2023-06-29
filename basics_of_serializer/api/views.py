from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.
def student_detail(request, id):
    stu = Student.objects.get(id = id) # complex obj
    serializer = StudentSerializers(stu) # python data
    json_data = JSONRenderer().render(serializer.data) # json Data
    return HttpResponse(json_data, content_type= 'application/json') # sending to the client
    # return JSONResponse(serializer.data) # igonre 12 and 13 line and use this if u want


# Create your views here.
def student_detail_home(request):
    stu = Student.objects.all() # complex obj
    serializer = StudentSerializers(stu, many = True) # converted to python data
    json_data = JSONRenderer().render(serializer.data) # converted to json Data
    return HttpResponse(json_data, content_type= 'application/json') # sending to the client
    # return JSONResponse(serializer.data) # igonre 12 and 13 line and use this if u want