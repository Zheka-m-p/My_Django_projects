from django.shortcuts import render
from . forms import FeedbackForm
from . models import Feedback

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# @login_required
def index(request):
    # 🔹 Проверяем, залогинен ли пользователь
    if not request.user.is_authenticated:
        # Если нет — показываем страницу с alert и кнопкой "Войти"
        return render(request, 'feedback/need_login.html')

    # 🔹 Проверяем, есть ли уже отзыв от этого пользователя, так как .exists() возвращает False, если записей нет
    feedback_exists = Feedback.objects.filter(user=request.user).exists()

    if feedback_exists: # если есть - показываем другой шаблон
        return render(request, 'feedback/already_submitted.html')

    if request.method == 'POST':
        form = FeedbackForm(request.POST) # сюда помещаем значения, которые пришли в пост-запросе
        if form.is_valid():
            feed = Feedback( # создаем объект - строку в таблице Feedback
                user=request.user,  # ✅ Добави это! иначе форма не работала(. забыф
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating'],
            )
            feed.save() # сохраняем ее в базу данных

            return HttpResponseRedirect(reverse('feedback:done')) # при редиректе теряются данные
    else:
        form = FeedbackForm() #  а в этом случае форма будет пустая
    return render(request, 'feedback/home_feedback.html', context={'form': form})

def done(request):
    return render(request, 'feedback/done.html')
