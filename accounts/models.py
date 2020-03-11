from django.db import models
from django.contrib.auth.models import User


class ProfessorCourses(models.Model):
    # username = models.CharField(max_length=30, unique=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
    )

    course1 = models.CharField(max_length=6, default=None, unique=True)
    course2 = models.CharField(max_length=6, default=None, unique=True)
    course3 = models.CharField(max_length=6, default=None, unique=True)
    course4 = models.CharField(max_length=6, default=None, unique=True)
    course5 = models.CharField(max_length=6, default=None, unique=True)


class StudentCourses(models.Model):
    # username = models.CharField(max_length=10, unique=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': False},
    )
    course1 = models.CharField(max_length=6, default=None, unique=True)
    course2 = models.CharField(max_length=6, default=None, unique=True)
    course3 = models.CharField(max_length=6, default=None, unique=True)
    course4 = models.CharField(max_length=6, default=None, unique=True)
    course5 = models.CharField(max_length=6, default=None, unique=True)


