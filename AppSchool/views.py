from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import models
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                "error": "Username and password are required"},
                status= status.HTTP_400_BAD_REQUEST
            )

        admin = models.Admin.objects.filter(username=username, password=password).first()
        
        if admin:
            return Response({
                "message": "Login successful",
                "user_type": "admin",
                "user_id": admin.id
            }, status=status.HTTP_200_OK)
        
        teacher = models.Teacher.objects.filter(username=username, password=password).first()

        if teacher:
            return Response({
                "message": "Login successful",
                "user_type": "teacher",
                "user_id": teacher.id
            }, status=status.HTTP_200_OK)
        
        return Response({
            "error": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED)
    
class CreateTeacherAdminView(APIView):
    def post(self, request):
        name = request.data.get("name")
        fullname = request.data.get("fullname")
        username = request.data.get("username")
        password = request.data.get("password")

        for field in [name, fullname, username, password]:
            if not field:
                return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        if models.Teacher.objects.filter(username=username).exists():
            return Response({"error":"The user already exists"}, status=status.HTTP_400_BAD_REQUEST)

        create_teacher = models.Teacher.objects.create(name=name, fullname=fullname, username=username, password=password)

        if create_teacher:
            return Response({
                "message": "Teacher created successfully",
                "teacher_id": create_teacher.id
            }, status=status.HTTP_201_CREATED)
        
        return Response({"error": "Failed to create teacher"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)