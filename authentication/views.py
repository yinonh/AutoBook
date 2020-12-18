from django.shortcuts import render

def signupuser(request):
    return render(request, 'authentication/signupuser.html')
