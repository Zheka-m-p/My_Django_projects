from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True) #blank = можно поле оставлять пустым при создании модели
    time_create = models.DateTimeField(auto_now_add=True) # заполняет автоматом, в момент создания записи
    time_update = models.DateTimeField(auto_now=True) # меняет поле, когда поле обнолвляется
    is_published = models.BooleanField(default=False) # опубликовано или нет(булево поле)

    def __str__(self):
        return self.title

'''
id: primary key (в модели не прописывается)
name: CharField - строка с максимальной длиной 100 символов; обязательное поле;
model: CharField - марка машины; обязательное поле;
price: IntegerField - цена машины с начальным значением 0; необязательное поле;
distance: IntegerField - пробег машины с начальным значением 0; необязательное поле;
is_exists: BooleanField - наличие товара (True - присутствует; False - отсутствует); по умолчанию True.

С помощью класса Auto добавьте в БД следующие машины в порядке их перечисления:

name="BMW X6"; model="BMW"; price=6000111;
name="Toyota Corolla"; model="Toyota"; distance=72000;
name="Haval 7"; model="Haval"; price=3500222;
'''

class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(default=0, blank=True)
    distance = models.IntegerField(default=0, blank=True)
    is_exists = models.BooleanField(default=True)

Auto.objects.create(name="BMW X6", model="BMW", price=6000111)
Auto.objects.create(name='Toyota Corolla', model='Toyota', distance=72000)
Auto.objects.create(name='Haval 7', model='Haval', price=3500222)

autos = Auto.objects.all()[:2]