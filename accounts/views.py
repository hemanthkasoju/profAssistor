from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('addQuestions')
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
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName,
                                                last_name=lastName)
                user.save()
                print("User created")
                return redirect('login')
        else:
            print('password not matching')
            return redirect('register')
    else:
        return render(request, 'register')





