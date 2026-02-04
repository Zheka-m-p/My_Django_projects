from django.urls import path
from .views import index
from .api import GetFilePath
# from . import views, api # - если потом пригодится много функций представлений

app_name = 'blog'

# Паттерны сайта
urlpatterns = [
    path('', index, name='home'),

]

# Паттерны API
urlpatterns += [
    path('bot/get-file/', GetFilePath.as_view()),
]