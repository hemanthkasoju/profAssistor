from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method =='POST' :
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']


        user = User.objects.create_user(username = username, password = password, email = email, first_name = firstName, last_name = lastName)
        user.save()
        print("User created")
        return redirect('/')
    else :
        return render(request, 'register.html')
