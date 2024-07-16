from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def overview(request):
    about = {
        "AppName": "RESTful API Basics",
        "Status": "Active",
    }
    return Response(about)