from django.shortcuts import render
from . forms import FeedbackForm
from . models import Feedback

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST) # сюда помещаем значения, которые пришли в пост-запросе
        if form.is_valid():
            print(form.cleaned_data) # очищенные данные
            feed = Feedback( # создаем объект - строку в таблице Feedback
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


def hello(request):
    res = request.GET # словарь
    print(res.get('name', 'кто ты?'))
    return HttpResponseRedirect(reverse('feedback:home')) # при редиректе теряются данные
    # return render(request, 'feedback/home_feedback.html')
