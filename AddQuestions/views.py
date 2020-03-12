from django.shortcuts import render, redirect
from .models import Question


def addQuestions(request):

    if request.method == 'POST':

        print(request.POST)
        question = request.POST['question']
        marks = request.POST['marks']
        difficulty = request.POST['difficulty']
        isImportant = request.POST['important']
        chapter: object = request.POST['chapter']
        time = request.POST['time']
        repeated = 0

        questionData = Question(question=question, marks=marks, difficulty=difficulty, isImportant=isImportant, chapter=chapter, time=time, repeated=repeated)

        questionData.save()
        print("Question added to database")
        return redirect('/addQuestions/')
    else:
        return render(request, 'addQuestions.html')




