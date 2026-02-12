from django import template
# from .. data_zodiac import ZODIAC_ICONS
from horoscope.data_zodiac import ZODIAC_ICONS

register = template.Library()

@register.filter
def zodiac_icon(zodiac_name):
    """Возвращает иконку для знака зодиака (если нет - знак вопроса)"""
    return ZODIAC_ICONS.get(zodiac_name, '?')
