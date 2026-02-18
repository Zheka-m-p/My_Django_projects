from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=50)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Отзыв'          # для одного объекта
        verbose_name_plural = 'Отзывы'   # для списка

    def __str__(self):
        return f"{self.name} {self.surname}, rating: {self.rating}"