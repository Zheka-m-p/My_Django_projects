from django.db import models

class Model(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True) #blank = можно поле оставлять пустым при создании модели
    time_create = models.DateTimeField(auto_now_add=True) # заполняет автоматом, в момент создания записи
    time_update = models.DateTimeField(auto_now=True) # меняет поле, когда поле обнолвляется
    is_published = models.BooleanField(default=False) # опубликовано или нет(булево поле)
