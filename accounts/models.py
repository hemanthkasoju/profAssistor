from django.db import models
from django.contrib.auth.models import User


class ProfessorCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    courseID = models.CharField(max_length=6, null=True)
    courseName = models.CharField(max_length=50, null=True)
    courseDescription = models.TextField()


class StudentCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    courseID = models.CharField(max_length=6, null=True)
    courseName = models.CharField(max_length=50, null=True)
    courseDescription = models.TextField()


