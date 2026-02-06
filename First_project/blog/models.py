from django.db import models

from django.urls import reverse
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


class PostFilesModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя файла')
    file = models.FileField(upload_to='post_files/')
    code = models.IntegerField(default=0, verbose_name='Код файла', unique=True)
    download_count = models.IntegerField(default=0, verbose_name='Скачиваний')

    class Meta:
        verbose_name = 'Файл поста'
        verbose_name_plural = 'Файлы постов'

    def increment_download_count(self):
        self.download_count += 1
        self.save()

    def __str__(self):
        return self.title


class BotUserModel(models.Model):
    chat_id = models.BigIntegerField(primary_key=True) #  уникальный номер пользователя в Телеграме
    first_name = models.CharField(max_length=50,     # Имя пользователя из Телеграма
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=50,    # Фамилия (необязательное поле - может быть пустым)
                                 blank=True,
                                 null=True,
                                 verbose_name='Фамилия')
    username = models.CharField(max_length=50,     # Username пользователя в Телеграме (@username)
                                blank=True,
                                null=True)
    created = models.DateTimeField(auto_now_add=True, # tекущая, локальная дата(дата сервера).
                                   verbose_name='Зарегистрирован')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Последняя активность')

    objects = models.Manager() # Менеджеры, это удобный способ взаимодействия с объектами в базе данных

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'

    def __str__(self):
        return self.first_name



class CategoryModel(MPTTModel):
    title = models.CharField(max_length=100,
                             verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Альт. заголовок")
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True,
                            verbose_name='Родительская категория')
    description = models.CharField(max_length=350,
                                   verbose_name="Описание",
                                   blank=True)

    objects = TreeManager()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = 'parent', 'slug'
        verbose_name = 'Категория поста'
        verbose_name_plural = 'Категории постов'

    def get_absolute_url(self):
        return reverse('blog:category_page', args=[int(self.pk), str(self.slug)])

    def __str__(self):
        return self.title

