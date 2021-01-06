from django.shortcuts import render, get_object_or_404,redirect
from Forum.models import Comments, Forum as forum

def Forum(request):
    forums = forum.objects.all()
    return render(request, 'Forum/Forum.html',{'forums':forums})

def comments(request,forum_id):
    currentForum = get_object_or_404(forum, pk=forum_id)
    commentim = Comments.objects.filter(forum=currentForum)
    return render(request, 'Forum/comments.html', {'forum': currentForum, 'commentim': commentim})
