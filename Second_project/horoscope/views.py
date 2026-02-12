from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .data_zodiac import data_zodiac, types_zodiac_dict


# Create your views here.
def index_horoscope(request):
    data = data_zodiac # передали весь список словарей в дату
    context = {
        'data': data
    }
    return render(request, 'horoscope/index_horoscope.html', context)


def get_info_about_sign_zodiac(request, sign_zodiac):
    data = [elem for elem in data_zodiac if elem['name'] == sign_zodiac] # получаем конкретный словарь знака зодиака
    if not data:
        context = {
            'error_message': f'Знак зодиака "{sign_zodiac}" не найден.',
            'show_home_link': True
        }
        return render(request, 'horoscope/error_page.html', context)
        # return HttpResponseNotFound(f'<h2>Неизвестный знак зодиака: {sign_zodiac}</h2>')
    context = {
        'data': data[0]
    }
    return render(request, 'horoscope/info_zodiac.html', context)


def get_info_about_sign_zodiac_by_number(request, number_zodiac):
    data = [elem for elem in data_zodiac if elem['number'] == number_zodiac] # так же знак зодиака, но уже по номеру
    if not data:
        context = {
            'error_message': f'Номер знака зодиака "{number_zodiac}" не найден.',
            'show_home_link': True
        }
        return render(request, 'horoscope/error_page.html', context)
        # return HttpResponseNotFound(f'<h2>Неизвестный номер зодиака: {number_zodiac}</h2>')
    return redirect('horoscope:sign_zodiac', sign_zodiac=data[0]['name'])


def type_zodiac(request):
    data = list(types_zodiac_dict) # 4 типа стихий получили (из ключей словаря)
    context = {
        'data': data
    }
    return render(request, 'horoscope/type_zodiac.html', context)


def type_element(request, type_element):
    data = [elem for elem in data_zodiac if elem['element'] == type_element] # словари, с переданным парамером стихии
    if not data:
        context = {
            'error_message': f'Неизвестный тип элемента: "{type_element}".',
            'show_home_link': True
        }
        return render(request, 'horoscope/error_page.html', context)
        # return HttpResponseNotFound(f'Неизвестный тип элемента: {type_element}')
    context = {
        'data': data
    }
    return render(request, 'horoscope/type_element.html', context)
