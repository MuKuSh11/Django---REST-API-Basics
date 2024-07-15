from rest_framework import serializers

from django.db.models import fields
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','school','age')