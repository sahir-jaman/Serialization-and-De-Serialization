from rest_framework import serializers
from .models import Student_model


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_model
        fields = ['id', 'name', 'roll', 'city']
