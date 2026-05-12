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

class CreateCourseAdminView(APIView):
    def post(self, request):
        name = request.data.get("name")
        parallel = request.data.get("parallel")

        for field in [name, parallel]:
            if not field:
                return Response({"error_empty": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if models.Course.objects.filter(name=name, parallel=parallel).exists():
            return Response({"error_exists": "The course already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        course = models.Course.objects.create(name=name, parallel=parallel)

        if course:
            return Response({
                "message": "Course created successfully",
                "course_id": course.id
            }, status=status.HTTP_201_CREATED)
        
        return Response({"error": "Failed to create course"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class CreateSubjectAdminView(APIView):
    def post(self, request):
        subject = request.data.get("name")

        if not subject:
            return Response({"error": "Subject name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if models.Subject.objects.filter(name=subject).exists():
            return Response({"error": "The subject already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_subject = models.Subject.objects.create(name=subject)

        if new_subject:
            return Response({
                "message": "Subject created successfully",
                "subject_id": new_subject.id
            }, status=status.HTTP_201_CREATED)

        return Response({"error": "Failed to create subject"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetTeacherAdminView(APIView):
    def get(self, request):
        teachers = models.Teacher.objects.all()
        if teachers:
            teacher_list = [ {"id": teacher.id, "name": teacher.name, "fullname": teacher.fullname, "username": teacher.username} for teacher in teachers]
            return Response({"teachers": teacher_list}, status=status.HTTP_200_OK)

        return Response({"error": "No teachers found"}, status=status.HTTP_404_NOT_FOUND)