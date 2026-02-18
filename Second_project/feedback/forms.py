from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя:', max_length=7, min_length=2,
                                            error_messages={'max_length': 'слишком много символов',
                                           'min_length': 'слишком malo символов',
                                           'required': 'укажите хотя бы 1 символ'})


    surname = forms.CharField(label='Фамилия:')
    feedback = forms.CharField(label='Отзыв:', widget=forms.Textarea(attrs={'rows':5, 'cols': 50}))
    rating = forms.IntegerField(label='Рейтинг:', max_value=5, min_value=1)