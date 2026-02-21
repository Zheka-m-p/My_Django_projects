from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) # Пользователь вводит только текст
        widgets = {
            # Настраиваем внешний вид поля ввода
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Напишите комментарий...',
                'class': 'form-control'
            }),
        }
