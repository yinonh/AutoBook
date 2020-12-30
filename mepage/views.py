from django.shortcuts import render

def meadult(request):
    return render(request, 'mepage/adult/mepageadult.html')
def meadultfavourites(request):
    return render(request, 'mepage/adult/favouritebooks.html')
def meadultpossesses(request):
    return render(request, 'mepage/adult/possessedbooks.html')
def mestudent(request):
    return render(request, 'mepage/student/mepagestudent.html')
def mestudentpossesses(request):
    return render(request, 'mepage/student/possessedbooks.html')
def mestudentevents(request):
    return render(request, 'mepage/student/events.html')
def mestudentlendedbooks(request):
    return render(request, 'mepage/student/lendedbooks.html')
