from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}, автор - {self.author}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Коммент от {self.author.username} к {self.post.title}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_like = models.BooleanField(default=True, verbose_name='Лайк (True) или дизлайк (False)')

    class Meta:
        verbose_name = 'Лайк/дизлайк'
        verbose_name_plural = 'Лайки/дизлайки'

    def __str__(self):
        action = 'лайк' if self.is_like else 'дизлайк'
        return f'{self.user.username} поставил {action} посту {self.post.title}'