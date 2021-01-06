from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,UserProfileForm,AdultProfileForm

def signupuser(request):
    if request.method == 'POST':
        ans = request.POST.get('kinduser')
        if ans == '1':
            return studentsignupuser(request)

        elif ans == '2':
            return adultsignupuser(request)
        else:
            return redirect("homepage")

    else:
        return render(request, 'authentication/signup2.html')

def studentsignupuser(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        print(form.errors)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print("befor")
            return redirect("homepage")
        print("after")
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}

    return render(request, 'authentication/signupuserstudent.html', context)
########################### adult



def adultsignupuser(request):
    if request.method == 'POST':
        form=ExtendedUserCreationForm(request.POST)
        profile_form=AdultProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile=profile_form.save(commit=False)
            profile.user = user

            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            print("befor")
            return redirect('homepage')
        print("after")
    else:
        form = ExtendedUserCreationForm()
        profile_form= AdultProfileForm()

    context= {'form': form, 'profile_form':profile_form}

    return render(request, 'authentication/signupuseradult.html', context)


def logoutuser(request):
    if request.method == "POST":
        logout(request)
    return redirect("homepage")


def loginU(request):
    if request.method == 'GET':
        return render(request, 'authentication/login.html', {'form': AuthenticationForm(), 'error': ""})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/login.html', {'form': AuthenticationForm(), 'error': "worng username or password"})
        else:
            login(request, user)
            return redirect('homepage')



