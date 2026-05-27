from django.http import HttpResponse
from django.shortcuts import render

def index(request): # request - это ссылка на класс НttpRequest, содержит инфу о запросе
    return HttpResponse("Страница приложения women")

def categories(request):
    return HttpResponse('<h1>Статьи по категории</h1>')