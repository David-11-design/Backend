from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AppSchool import views

urlpatterns = [
    path('students/', views.LoginView.as_view()),
    path('create-teacher/', views.CreateTeacherAdminView.as_view()),
    ]