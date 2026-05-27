from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # request - это ссылка на класс НttpRequest, содержит инфу о запросе
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категории</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категории</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')
