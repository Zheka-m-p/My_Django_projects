from django.db import models
from django.urls import reverse # полезная штука, но вечно забываю...

# Create your models here.
class Producer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    producer_email = models.EmailField(max_length=50, verbose_name='email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'


class Movie(models.Model):
    EURO = 'EURO'
    DOLLAR = 'DOLLAR'
    RUB = 'RUB'

    VALUTE_CHOICES = [
        (EURO, 'EUR'),
        (DOLLAR, 'DOL'),
        (RUB, 'RUB'),
    ]

    # атрибуты класса - как колонки в таблице (id - автоматически создается)
    name = models.CharField(max_length=40, verbose_name='Название фильма')
    rating = models.IntegerField(verbose_name='рейтинг фильма')
    year = models.IntegerField(verbose_name='год выпуска', null=True)
    budget = models.IntegerField(verbose_name='бюджет фильма', default=1000000)
    currency = models.CharField(max_length=6, verbose_name='валюта', choices=VALUTE_CHOICES, default=DOLLAR)

    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True) # для связи с другой таблицей

    def get_absolute_url(self):
        '''Для получения ссылки на наш одиночный фильм'''
        return reverse('movie:solo_movie', args=[self.id])

    def __str__(self):
        return f'{self.name}: рейтинг - {self.rating}'


    class Meta:  # ← Это внутренний класс Meta
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

