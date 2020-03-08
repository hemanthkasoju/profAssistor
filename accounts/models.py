from django.db import models


class ProfessorCourses(models.Model):
    username = models.CharField(max_length=30, unique=True)
    course1 = models.CharField(max_length=6, default=None)
    course2 = models.CharField(max_length=6, default=None)
    course3 = models.CharField(max_length=6, default=None)
    course4 = models.CharField(max_length=6, default=None)
    course5 = models.CharField(max_length=6, default=None)


class StudentCourses(models.Model):
    username = models.CharField(max_length=10, unique=True)
    course1 = models.CharField(max_length=6, default=None)
    course2 = models.CharField(max_length=6, default=None)
    course3 = models.CharField(max_length=6, default=None)
    course4 = models.CharField(max_length=6, default=None)
    course5 = models.CharField(max_length=6, default=None)
