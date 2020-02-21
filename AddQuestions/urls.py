from django.urls import path
from . import views

urlpatterns = [
    path('addQuestions/', views.addQuestions, name = 'addQuestions'),
]
