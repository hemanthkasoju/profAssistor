from django.db import models

class Question(models.Model):
    question=models.TextField()
    marks=models.IntegerField()
    difficulty=models.IntegerField()
    isImportant=models.BooleanField(default=False)
    chapter=models.IntegerField()
    time=models.IntegerField()

# Create your models here.
