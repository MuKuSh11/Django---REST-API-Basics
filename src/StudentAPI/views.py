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
        "/all": "Get all objects",
        "/add": "To add new data",
        "/modify/<id>": "To modify data, you need to pass all the fields",
        "/patch/<id>": "To modify data, all the fields not required",
        "/delete/<id>": "To delete data",
    }
    return Response(about)

@api_view(['POST'])
def add_data(request):
    received_data = request.data
    studentData = StudentSerializer(data = received_data)
    print(type(studentData))

    if studentData.is_valid():
        studentData.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def modify_data(request, id):
    student = Student.objects.get(id = id)
    studentData = StudentSerializer(instance = student, data = request.data)

    if studentData.is_valid():
        studentData.save()
        return Response(studentData.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def patch_data(request, id):
    student = Student.objects.get(id = id)
    studentData = StudentSerializer(instance = student, data = request.data, partial = True)

    if studentData.is_valid():
        studentData.save()
        return Response(studentData.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all(request):
    students = Student.objects.all()

    if students:
        serializedData = StudentSerializer(students, many = True)
        return Response(serializedData.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_data(request, id):
    student = Student.objects.get(id = id)
    if student:
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
