from django import forms

from comments.models import *


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)