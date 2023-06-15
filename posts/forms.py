from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import *

class AddPostForm(forms.ModelForm):
    # всязь формы с моделью
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    visible_to = forms.ChoiceField(
        choices=Post.VISIBLE_TO_CHOICES,
        initial='all',
        widget=forms.RadioSelect(attrs={'class': 'form-input'}),
        label='Видимость поста'
    )
#     # Валидатор (проверка на ошибки полей формы)
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if len(title) > 255:
#             raise ValidationError('Длинна превишает 200 символов')
#
        # return title