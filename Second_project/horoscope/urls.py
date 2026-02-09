from django.urls import path
from . import views

app_name = 'horoscope'

urlpatterns = [
    path('<sign_zodiac>/', views.get_info_about_zodiac_sign),
    path('sign/<int:pk>/', views.sign),

    # path('leo/', views.leo),
    # path('scorpion/', views.scorpion),
]