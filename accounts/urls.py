from django.urls import path
from .import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("studentLogin", views.studentLogin, name="studentLogin"),
    path("studentRegister", views.studentRegister, name="studentRegister"),
    path("logout", views.logout, name="logout"),
    path("createCourse", views.createCourse, name="createCourse"),
    path("profHomePage", views.profHomePage, name="profHomePage"),
    path("studentHomePage", views.studentHomePage, name="studentHomePage"),
    path("courseHome", views.courseHome, name="courseHome"),
    path('courseHome/<courseID>', views.courseHome, name='courseHome')

]
