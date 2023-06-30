from django.contrib import admin
from .models import Student_model

# Register your models here.
@admin.register(Student_model)
class Student_admin(admin.ModelAdmin):
    list_display=['id', 'name', 'roll', 'city']


