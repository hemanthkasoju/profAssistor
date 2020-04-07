from django.db.models import Sum
from django.shortcuts import render, redirect
from AddQuestions.models import Question
from django.http import HttpResponse
from profAssistor.utils import render_to_pdf
from django.template.loader import get_template
from django.contrib import messages


def selectQuestionPreference(request):
    if request.method == 'POST':
        courseID = request.session.get("courseID")
        difficulty = request.POST['difficulty']
        marks = request.POST['marks']
        chapter = request.POST['chapter']
        template = get_template('renderPDF.html')
        questions = Question.objects.filter(courseID=courseID, difficulty=difficulty, chapter=chapter).order_by(
            '-marks')
        totalMarks = questions.aggregate(Sum('marks'))

        if totalMarks.get('marks__sum') is None:
            messages.info(request, 'No questions added')

            return redirect('selectQuestionPreference')

        if int(marks) > totalMarks.get('marks__sum'):
            messages.info(request, 'Exceeds total marks. Please select within ' + str(totalMarks.get('marks__sum')))

            return redirect('selectQuestionPreference')
        else:
            print("Total marks : ", totalMarks.get('marks__sum'))
            selectMarks = 0
            previousTotal = 0
            nextTotal = 0
            selectQuestions = []
            for question in questions:

                # if selectMarks + int(question.marks) <= int(marks):
                if selectMarks <= int(marks):

                    previousTotal = selectMarks
                    selectQuestions.append(question)
                    selectMarks += int(question.marks)
                    print(selectMarks)
                    if selectMarks == int(marks):
                        print("Equal")
                        print("marks :", selectMarks)
                        break
                    elif selectMarks > int(marks):
                        nextTotal = selectMarks

            if selectMarks == int(marks):
                context = {
                    "questions": selectQuestions,
                    "marks": selectMarks
                }
                print(context)
                html = template.render(context)
                pdf = render_to_pdf('renderPDF.html', context)

                return HttpResponse(pdf, content_type='application/pdf')
            else:
                messages.info(request,
                              'Your marks did not match combination. select ' + str(previousTotal) + " or " + str(
                                  nextTotal))
                return redirect('selectQuestionPreference')

    else:
        print("This is get")
        return render(request, 'questionPreference.html')


def assignmentPreference(request):
    if request.method == 'POST':
        courseID = request.session.get("courseID")
        difficulty = request.POST['difficulty']
        marks = request.POST['marks']
        chapter = request.POST['chapter']
        template = get_template('renderPDF_1.html')
        questions = Question.objects.filter(courseID=courseID, difficulty=difficulty, chapter=chapter,
                                            isImportant=True).order_by('-marks')
        totalMarks = questions.aggregate(Sum('marks'))

        if totalMarks.get('marks__sum') is None :
            messages.info(request, 'No questions added')

            return redirect('assignmentPreference')


        if int(marks) > totalMarks.get('marks__sum'):
            messages.info(request, 'Exceeds total marks. Please select within ' + str(totalMarks.get('marks__sum')))

            return redirect('assignmentPreference')
        else:
            print("Total marks : ", totalMarks.get('marks__sum'))
            selectMarks = 0
            previousTotal = 0
            nextTotal = 0
            selectQuestions = []
            for question in questions:

                if selectMarks <= int(marks):

                    previousTotal = selectMarks
                    selectQuestions.append(question)
                    selectMarks += int(question.marks)
                    print(selectMarks)
                    if selectMarks == int(marks):
                        print("Equal")
                        print("marks :", selectMarks)
                        break
                    elif selectMarks > int(marks):
                        nextTotal = selectMarks

            if selectMarks == int(marks):
                context = {
                    "questions": selectQuestions,
                    "marks": selectMarks
                }
                print(context)
                html = template.render(context)
                pdf = render_to_pdf('renderPDF_1.html', context)

                return HttpResponse(pdf, content_type='application/pdf')
            else:
                messages.info(request,
                              'Your marks did not match combination. select ' + str(previousTotal) + " or " + str(
                                  nextTotal))
                return redirect('assignmentPreference')

    else:
        print("This is get")
        return render(request, 'assignmentPreference.html')
