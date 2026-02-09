from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def leo(request):
    return HttpResponse('Знак зодиака лев')


def scorpion(request):
    return HttpResponse('Знак зодиака scorpion')

def sign(request, pk):
    context = {
        'pk':pk
    }
    return HttpResponse(f'{context} fsfa')

def get_info_about_zodiac_sign(request, sign_zodiac):
    zodiac_descriptions = {
        'leo': 'Знак зодиака лев',
        'scorpion': 'Знак зодиака скорпион',
        'taurus': 'Знак зодиака телец',
        # ... добавитьь остальные 9 знаков
    }

    description = zodiac_descriptions.get(sign_zodiac.lower())

    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака {sign_zodiac}')