from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'authentication/signupuser.html', {'form': UserCreationForm(), 'error': ""})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homepage')
        except IntegrityError:
            return render(request, 'authentication/signupuser.html', {'form': UserCreationForm(), 'error': "this username alredy taken"})
        else:
            return render(request, 'authentication/signupuser.html', {'form': UserCreationForm(), 'error': "Password did not match"})

def logoutuser(request):
    if request.method == "POST":
        logout(request)
    return redirect("homepage")

def login(request):
    if request.method == 'GET':
        return render(request, 'authentication/signupuser.html', {'form': AuthenticationForm(), 'error': ""})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/login.html', {'form': AuthenticationForm(), 'error': "worng username or password"})
        else:
            login(request, user)
            return redirect('homepage')


