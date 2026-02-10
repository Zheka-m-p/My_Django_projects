from django.urls import path
from . import views

app_name = 'horoscope'

urlpatterns = [
    path('', views.index_horoscope, name='index_horoscope'),
    path('<int:number_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='zodiac'),

]