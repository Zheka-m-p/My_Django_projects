from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

zodiac_descriptions = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_numbers = dict(zip(range(1, len(zodiac_descriptions) + 1), list(zodiac_descriptions.keys())))

# Create your views here.
def get_info_about_zodiac_sign(request, sign_zodiac): # можно совместить с вьюхой выше, но пока пусть так
    description = zodiac_descriptions.get(sign_zodiac.lower())
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака: {sign_zodiac}')


def get_info_about_zodiac_sign_by_number(request, number_zodiac):
    zodiac = zodiac_numbers.get(number_zodiac) # получаем имя зодиака-строку (или None)
    if zodiac:
        return redirect('horoscope:zodiac', sign_zodiac=zodiac)
    else:
        return HttpResponseNotFound(f'Нет знака зодиака с номером: {number_zodiac}')
    # return get_info_about_zodiac_sign(request, zodiac)