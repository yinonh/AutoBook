from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def simple (request):
    return render(request, 'home/simple.html')
