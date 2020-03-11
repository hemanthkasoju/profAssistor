from django.db import models


class Question(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    difficulty = models.IntegerField()
    isImportant = models.BooleanField(default=False)
    chapter = models.IntegerField()
    time = models.IntegerField()
    repeated = models.IntegerField()
    isSelected = models.BooleanField(default=False)
    courseID = models.TextField()
