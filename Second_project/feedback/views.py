from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'feedback/home_feedback.html')


def hello(request):
    res = request.GET # словарь
    print(res.get('name', 'кто ты?'))
    return HttpResponseRedirect(reverse('feedback:home'))
    # return render(request, 'feedback/home_feedback.html')
