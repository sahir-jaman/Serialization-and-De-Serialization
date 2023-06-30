from django.contrib import admin
from .models import Student_for_crud

# Register your models here.
@admin.register(Student_for_crud)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'roll', 'city']