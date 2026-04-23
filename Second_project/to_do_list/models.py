from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Юзер')

    title = models.CharField(max_length=100, verbose_name='Название задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    complete = models.BooleanField(default=False, verbose_name='Выполнена')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['complete', 'created_at']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

