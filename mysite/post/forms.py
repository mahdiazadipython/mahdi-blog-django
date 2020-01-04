from django import forms
from.models import Comment,Book

class  CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        
        fields = ("name","email","body")


