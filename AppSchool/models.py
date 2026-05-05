from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class Student(models.Model):
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.fullname


class Course(models.Model):
    name = models.CharField(max_length=100)
    parallel = models.CharField(max_length=50)

    teachers = models.ManyToManyField(Teacher, related_name="courses")

    def __str__(self):
        return f"{self.name} - {self.parallel}"


class Subject(models.Model):
    name = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course, related_name="subjects")

    def __str__(self):
        return self.name


class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="notes")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="notes")

    note1 = models.IntegerField(null=True, blank=True)
    note2 = models.IntegerField(null=True, blank=True)
    note3 = models.IntegerField(null=True, blank=True)
    note4 = models.IntegerField(null=True, blank=True)
    leccion = models.IntegerField(null=True, blank=True)
    examen = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"