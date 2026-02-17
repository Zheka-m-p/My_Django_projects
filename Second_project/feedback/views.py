from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'unknown_name')
        print(f'имя: {name}')
        if len(name) == 0: # минимальная обработка формы
            return render(request, 'feedback/home_feedback.html', context={'got_error': True})
        return HttpResponseRedirect(reverse('feedback:done')) # при редиректе теряются данные

    return render(request, 'feedback/home_feedback.html', context={'got_error': False})

def done(request):
    return render(request, 'feedback/done.html')


def hello(request):
    res = request.GET # словарь
    print(res.get('name', 'кто ты?'))
    return HttpResponseRedirect(reverse('feedback:home')) # при редиректе теряются данные
    # return render(request, 'feedback/home_feedback.html')
