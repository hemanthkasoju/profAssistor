from django.shortcuts import render, redirect
from AddQuestions.models import Question

def selectQuestionPreference(request):

    # if request.method == 'POST':
    print("This is post")
    questions = Question.objects.all()
    selectedQuestions = []
    # difficulty = request.POST['difficulty']

        # for question in questions:
        #     if question.difficulty == difficulty:
        #         selectedQuestions.append(question)
        #         print(question.question)

    return render(request, 'displayQuestions.html', {'questions' : questions})

    # else:
    #     print("This is get")
    #     return render(request, 'questionPreference.html')