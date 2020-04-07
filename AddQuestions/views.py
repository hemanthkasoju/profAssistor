from django.shortcuts import render, redirect
from .models import Question
from django.contrib import messages
from django.contrib.auth.models import User


def addQuestions(request):
    if request.method == 'POST':

        print(request.session.get("courseID"))
        courseID = request.session.get("courseID")
        question = request.POST['question']
        marks = request.POST['marks']
        difficulty = request.POST['difficulty']
        isImportant = request.POST['important']
        chapter: object = request.POST['chapter']
        time = request.POST['time']
        repeated = 0

        if Question.objects.filter(question=question).exists():
            print("Question already added")
            messages.info(request, 'Question already added')
            return redirect('addQuestions')
        else:
            questionData = Question(question=question, marks=marks, difficulty=difficulty, isImportant=isImportant,
                                    chapter=chapter, time=time, repeated=repeated, courseID=courseID)

            questionData.save()
            print("Question added to database")
            messages.info(request, 'Question added to database')
            return redirect('addQuestions')
    else:

        return render(request, 'addQuestions.html')
