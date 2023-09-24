from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.


def homepage(request):
    return render(request, "home.html")


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get('confirmpassword')
        if password != password2:
            return HttpResponse("Your password did't match ")
        else:
            my_user = User.objects.create_user(uname, email, password)
            my_user.save()
            return redirect("login")


    return render(request, "signup.html")


def loginpage(request):
    if request.method=="POST":
        username=request.POST,get("username")
        pass1=request.POST,get("pass")
        print(username,pass1)

        
    return render(request, "login.html") 
