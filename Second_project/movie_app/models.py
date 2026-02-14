from django.db import models
from django.urls import reverse # полезная штука, но вечно забываю...

# Create your models here.
class Movie(models.Model):
    # атрибуты класса - как колонки в таблице (id - автоматически создается)
    name = models.CharField(max_length=40, verbose_name='Название фильма')
    rating = models.IntegerField(verbose_name='рейтинг фильма')
    year = models.IntegerField(verbose_name='год выпуска', null=True)
    budget = models.IntegerField(verbose_name='бюджет фильма', default=1000000)

    def get_absolute_url(self):
        '''Для получения ссылки на наш одиночный фильм'''
        return reverse('movie:solo_movie', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

    class Meta:  # ← Это внутренний класс Meta
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

