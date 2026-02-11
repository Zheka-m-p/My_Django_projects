from django.urls import path
from . import views

app_name = 'horoscope'

urlpatterns = [
    path('', views.index_horoscope, name='home_horoscope'),
    # переходим на шаблоны
    path('type/', views.type_zodiac, name='types_element_zodiac'),
    path('type/<str:type_element>/', views.type_element, name='type_element'),

    path('<int:number_zodiac>/', views.get_info_about_sign_zodiac_by_number, name='number_zodiac'),#
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='sign_zodiac'),#

]