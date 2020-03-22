from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import ProfessorCourses, StudentCourses


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_staff=True)
        if user is not None:
            auth.login(request, user)

            return redirect('profHomePage')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                print("Username taken")
                messages.info(request, 'Username Taken')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName,
                                                last_name=lastName, is_staff=True)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def createCourse(request):
    if request.method == 'POST':
        ProfessorCourses.objects.create(courseID=request.POST['courseID'],
                                        user_id=request.user.id,
                                        courseName=request.POST['courseName'],
                                        courseDescription=request.POST['description'])

        print("Course added to database")
        return redirect('profHomePage')
    else:
        return render(request, "createCourse.html")


def profHomePage(request):
    userID = request.user.id
    print(userID)
    profCourses = ProfessorCourses.objects.filter(user_id=userID)
    return render(request, "profHomePage.html", {'profCourses': profCourses})


def courseHome(request, courseID):
    print(courseID)
    request.session["courseID"] = courseID
    return render(request, "courseHomePage.html")


def studentLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_staff=False)
        if user is not None:
            auth.login(request, user)

            return redirect('studentHomePage')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('studentLogin')

    else:
        return render(request, "studentLogin.html")


def studentRegister(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                print("Username taken")
                messages.info(request, 'Username Taken')
                return redirect('studentRegister')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('studentRegister')

            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName,
                                                last_name=lastName, is_staff=False)
                user.save()
                print("User created")
                return redirect('studentLogin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('studentRegister')
    else:
        return render(request, 'studentLogin.html')


def studentHomePage(request):
    student = request.user
    studentCourses = StudentCourses.objects.filter(user_id=student.id)
    return render(request, 'studentHomePage.html', {'student': student, "studentCourses": studentCourses})


def studentCourseRegister(request):
    if request.method == 'POST':
        courseID = request.POST['courseID']

        if ProfessorCourses.objects.filter(courseID=courseID).exists():

            StudentCourses.objects.create(courseID=courseID, user_id=request.user.id)
            print("Course added to database")
            return redirect('studentHomePage')
        else:
            messages.info(request, 'Course not available')
            return redirect('studentCourseRegister')

    else:
        return render(request, "courseRegister.html")


def studentCourseHome(request, courseID) :
    print(courseID)
    return render(request, "studentCourseHome.html")
