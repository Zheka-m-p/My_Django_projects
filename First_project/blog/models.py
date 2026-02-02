from django.db import models

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

