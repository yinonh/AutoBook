from Forum.models import Forum, Comments
from django import forms

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'text']

class CommitForum(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'text']