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
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):  # request - это ссылка на класс НttpRequest, содержит инфу о запрос
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0
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


def show_category(request, cat_id):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
