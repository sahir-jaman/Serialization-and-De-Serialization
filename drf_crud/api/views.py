from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student_for_crud
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


# class based views is here:
@method_decorator(csrf_exempt, name='dispatch')
class student_info(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        uid = python_data.get('id', None) # either id or None would be the ans here.
        if uid is not None:
            stu = Student_for_crud.objects.get(id=uid)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            stu = Student_for_crud.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data inserted successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type= 'application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type= 'application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student_for_crud.objects.get(id = id)
        serializer = StudentSerializer(stu, data=python_data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        uid = python_data.get('id')
        stu = Student_for_crud.objects.get(id=uid)
        stu.delete()
        res = {'msg': 'Data Deleted successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


# # Fucntion based views is here.
# @csrf_exempt
# def student_info(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         uid = python_data.get('id', None) # either id or None would be the ans here.
#         if uid is not None:
#             stu = Student_for_crud.objects.get(id=uid)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             stu = Student_for_crud.objects.all()
#             serializer = StudentSerializer(stu, many=True)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data inserted successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type= 'application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type= 'application/json')

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student_for_crud.objects.get(id = id)
#         serializer = StudentSerializer(stu, data=python_data ,partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data updated successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         uid = python_data.get('id')
#         stu = Student_for_crud.objects.get(id=uid)
#         stu.delete()
#         res = {'msg': 'Data Deleted successfully'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')

