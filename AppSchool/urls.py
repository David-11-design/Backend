from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AppSchool import views

urlpatterns = [
    path('students/', views.LoginView.as_view()),
    path('create-Teacher/', views.CreateTeacherAdminView.as_view()),
    path('Create-Course/', views.CreateCourseAdminView.as_view()),
    path('Create-Subject/', views.CreateSubjectAdminView.as_view()),
    path('Get-Teachers/', views.GetTeacherAdminView.as_view()),
    ]