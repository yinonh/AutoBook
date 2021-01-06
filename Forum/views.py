from django.shortcuts import render, get_object_or_404,redirect
from Forum.models import Comments, Forum as forum
from Forum.forms import ForumForm,CommitForum


def Forum(request):
    forums = forum.objects.all()
    if request.method == "GET":
        return render(request, 'Forum/Forum.html',{'forums':forums,"form":ForumForm()})
    elif request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.student = request.user.student
            newForm.save()
            return redirect("Forum")
        else:
            return render(request, 'Forum/Forum.html', {'forums': forums, "form": ForumForm(),"error":"bad data"})


def comments(request,forum_id):
    currentForum = get_object_or_404(forum, pk=forum_id)
    if request.method == "GET":
        commentim = Comments.objects.filter(forum=currentForum)
        return render(request, 'Forum/comments.html', {'forum': currentForum, 'commentim': commentim, "form": CommitForum()})
    elif request.method == "POST":
        form = CommitForum(request.POST)
        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.student = request.user.student
            newComment.forum = currentForum
            newComment.save()
            return redirect("comments", forum_id)
        else:
            return render(request, 'Forum/comments.html', {'forums': forums, "form": ForumForm(), "error": "bad data"})