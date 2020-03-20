from django.shortcuts import render, redirect
from AddQuestions.models import Question


def selectQuestionPreference(request):
    if request.method == 'POST':
        courseID = request.session.get("courseID")
        questions = Question.objects.filter(courseID=courseID)
        time = request.POST['time']
        password = request.POST['password']
        difficulty = request.POST['difficulty']
        marks = request.POST['marks']

        return render(request, 'displayQuestions.html', {'questions': questions})

    else:
        print("This is get")
        return render(request, 'questionPreference.html')
