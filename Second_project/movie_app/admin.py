from django.contrib import admin
from . models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'year', 'budget', 'currency','rating_status')  # добавляем нужные нам колонки для отображения на сайте
    search_fields = ('name', 'year',)  # добавляем поле поиска по данным колонкам
    list_filter = ('budget', 'year',)  # добавляем фильтр по данной колонке, можем добавлять несколько фильтров

    list_editable = ( 'rating', 'year', 'budget', 'currency',) # чтобы изменять на месте, не переходя на конкретный фильм
    # ordering = ('name', ) # сортировать по имени фильма
    # list_per_page = 3 # пагинация - по 3 фильма на странице

    @admin.display(ordering='rating') # для сортировки
    def rating_status(self, movie: Movie): # 2 параметр(после self) - это экземпляр класса модели Movie
        if movie.rating < 50:
            return 'Зачем это смотреть'
        elif 50 <= movie.rating < 75:
            return 'На разок'
        elif 75 <= movie.rating < 85:
            return 'Можно посмотреть'
        return 'Топ'