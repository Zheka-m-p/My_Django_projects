from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):  # request - это ссылка на класс НttpRequest, содержит инфу о запросе
    return render(request, 'women/index.html')


def about(request):
    return render(request, 'women/about.html')


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
    if year > 2025:
        # return redirect('/', permanent=True) # редирект по адресу
        # return redirect(index) # по имени функции
        # return redirect('home') # по имени маршрута url
        # return redirect('cats_slug', 'music') # по имени с параметрами запроса
        # return HttpResponseRedirect('/') # или же HttpResponsePermanentRedirect(на 301)

        url = reverse('cats_slug', args=('music',))
        return redirect(url)
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
