from django.urls import path
# from .views import index
# from .api import GetFilePath
from . import views, api # - если потом пригодится много функций представлений

app_name = 'blog'

# Паттерны сайта
urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:pk>-<str:slug>/', views.category_page, name='category_page'),
    path('post/<int:pk>-<str:slug>/', views.post_page, name='post_page'),

]

# Паттерны API
urlpatterns += [
    path('bot/get-file/', api.GetFilePath.as_view()),
    path('bot/create-user/', api.CreateBotUser.as_view()),
]