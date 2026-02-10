from django.urls import path
from . import views

app_name = 'horoscope'

urlpatterns = [
    path('', views.index_horoscope, name='index_horoscope'),

    path('type/<str:type_element>/', views.type_element, name='type_element'),
    path('type/', views.type_zodiac, name='type_zodiac'),

    path('<int:number_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='zodiac'),

]