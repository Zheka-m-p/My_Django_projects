from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):  # request - это ссылка на класс НttpRequest, содержит инфу о запросе
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):
    if cat_id <= 0:
        raise Http404()
    return HttpResponse(f'<h1>Статьи по категории</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        dict_ = dict(request.GET)

        params = [f'{k}={v[0]}' for k, v in dict_.items()]
        res = '|'.join(params)
        print(res)
        return HttpResponse(f"{res}")
    else:
        return HttpResponse('GET is empty')

    return HttpResponse(f'<h1>Статьи по категории</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
