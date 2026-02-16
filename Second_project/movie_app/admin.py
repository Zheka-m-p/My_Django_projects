from django.contrib import admin, messages
from . models import Movie
from django.db.models import QuerySet

# Register your models here.
class RatingMovieFilter(admin.SimpleListFilter):
    title = 'Рейтинг:'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('меньше 40-ка', 'Низкий'), # (значение, название_значения)
            ('от 40 до 59', 'Средний'), # (значение, название_значения)
            ('от 60 до 80',  'Высокий'), # (значение, название_значения)
            ('Больше 80-ти',  'Топчик'), # (значение, название_значения)
        ]

    def queryset(self, request, queryset: QuerySet): # QuerySet - коллекция всех записей муви
        if self.value() == 'меньше 40-ка': # проверям на равенство значению, которые мы сами задани
            return queryset.filter(rating__lt=40)
        elif self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40, rating__lte=59)
        elif self.value() == 'от 60 до 80':
            return queryset.filter(rating__gte=60, rating__lte=80)
        elif self.value() == 'Больше 80-ти':
            return queryset.filter(rating__gt=80)
        return queryset# ← если не выбран фильтр


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'year', 'budget', 'currency','rating_status')  # добавляем нужные нам колонки для отображения на сайте
    search_fields = ('name', 'year',)  # добавляем поле поиска по данным колонкам
    list_filter = ('budget', 'currency', RatingMovieFilter)  # добавляем фильтр по данной колонке, можем добавлять несколько фильтров

    list_editable = ( 'rating', 'year', 'budget', 'currency',) # чтобы изменять на месте, не переходя на конкретный фильм
    # ordering = ('name', ) # сортировать по имени фильма
    # list_per_page = 3 # пагинация - по 3 фильма на странице
    actions = ('set_dollars', 'set_euro', )


    @admin.display(ordering='rating') # для сортировки
    def rating_status(self, movie: Movie): # 2 параметр(после self) - это экземпляр класса модели Movie
        if movie.rating < 50:
            return 'Зачем это смотреть'
        elif 50 <= movie.rating < 75:
            return 'На разок'
        elif 75 <= movie.rating < 85:
            return 'Можно посмотреть'
        return 'Топ'

    @admin.action(description='Установить валюты в доллары')
    def set_dollars(self, request, qs: QuerySet):
        '''Добавляет новое действие в админку: а именно, меняет все значения валют на доллары'''
        qs.update(currency=Movie.DOLLAR)

    @admin.action(description='Установить валюты в евро')
    def set_euro(self, request, qs: QuerySet):
        '''Добавляет новое действие в админку: а именно, меняет все значения валют на евро'''
        count_updated =  qs.update(currency=Movie.EURO)
        self.message_user(request, message=f'Было обновлено {count_updated} записей!', level=messages.ERROR)