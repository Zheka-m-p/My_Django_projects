from django.contrib import admin
from . import models


# Регистрируем модель в админке Django
@admin.register(models.PostFilesModel)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'download_count',)  # Какие поля показывать в списке объектов
    search_fields = ('title',)  # По каким полям можно искать
    readonly_fields = ('download_count',)  # Поле, которое видно, но нельзя редактировать

    # exclude = ('download_count',)  # Какие поля скрыть при создании/редактировании


@admin.register(models.BotUserModel)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'first_name', 'last_name', 'username', 'created', 'updated')
    search_fields = ['chat_id', 'first_name', 'username', ]