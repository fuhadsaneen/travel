from django.http import HttpResponse
from django.shortcuts import render
from .models import place,person
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def demo(request):
    res=place.objects.all()
    res1=person.objects.all()
    return render(request,"index.html",{'result':res,'result1':res1})
def register(request):
    if request.method == 'POST':
        username = request.POST['user']
        first = request.POST['first']
        last = request.POST['last']
        mail = request.POST['mail']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first, last_name=last, email=mail,
                                                password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password not macth')
            return redirect('register')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('correct')
            return redirect('demo')
        else:
            messages.info(request, 'inavailid')
            print('invalid')
            return redirect('login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
