from django.shortcuts import render, redirect
from AddQuestions.models import Question
from django.http import HttpResponse
from profAssistor.utils import render_to_pdf
from django.template.loader import get_template


def selectQuestionPreference(request):
    if request.method == 'POST':
        courseID = request.session.get("courseID")
        questions = Question.objects.filter(courseID=courseID)
        time = request.POST['time']
        difficulty = request.POST['difficulty']
        marks = request.POST['marks']
        chapter = request.POST['chapter']
        template = get_template('renderPDF.html')
        context = {
            "questions" : questions
        }
        html = template.render(context)
        pdf = render_to_pdf('renderPDF.html', context)

        return HttpResponse(pdf, content_type='application/pdf')

        # return render(request, 'displayQuestions.html', {'questions': questions})

    else:
        print("This is get")
        return render(request, 'questionPreference.html')


def generatePDF(request, *args, **kwargs):
    template = get_template('renderPDF.html')
    context = {
        "id": 10,
    }
    html = template.render(context)
    pdf = render_to_pdf('renderPDF.html', context)
    return HttpResponse(pdf, content_type='application/pdf')