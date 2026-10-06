from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import slugify, slice_filter

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def index(request):  # request - это ссылка на класс НttpRequest, содержит инфу о запрос
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'title': 'О сайте', 'menu': menu}
    return render(request, 'women/about.html', data)


def addpage(request):
    return HttpResponse(f'Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


# def categories(request, cat_id):
#     if cat_id <= 0:
#         raise Http404()
#     return HttpResponse(f'<h1>Статьи по категории</h1><p>id: {cat_id}</p>')


# def categories_by_slug(request, cat_slug):
#     if request.GET:
#         dict_ = dict(request.GET)
#
#         params = [f'{k}={v[0]}' for k, v in dict_.items()]
#         res = '|'.join(params)
#         print(res)
#         return HttpResponse(f"{res}")
#     else:
#         return HttpResponse('GET is empty')
#
#     return HttpResponse(f'<h1>Статьи по категории</h1><p>slug: {cat_slug}</p>')


# def archive(request, year):
#     if year > 2025:
#         # return redirect('/', permanent=True) # редирект по адресу
#         # return redirect(index) # по имени функции
#         # return redirect('home') # по имени маршрута url
#         # return redirect('cats_slug', 'music') # по имени с параметрами запроса
#         # return HttpResponseRedirect('/') # или же HttpResponsePermanentRedirect(на 301)
#
#         url = reverse('cats_slug', args=('music',))
#         return redirect(url)
#     return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
