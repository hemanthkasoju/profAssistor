from django.shortcuts import render

# Create your views here.

def addQuestions(request) :
    return render(request, 'addQuestions.html')
