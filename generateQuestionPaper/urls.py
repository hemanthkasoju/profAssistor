from django.urls import path
from . import views

urlpatterns = [

    path('selectQuestionPreference', views.selectQuestionPreference, name='selectQuestionPreference'),
]
