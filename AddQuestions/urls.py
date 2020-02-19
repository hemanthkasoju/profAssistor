from django.urls import path
from . import views

urlpatterns = [
    path('', views.addQuestions, name = 'addQuestions'),
]
