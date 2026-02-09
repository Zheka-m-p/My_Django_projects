from django.urls import path
from . import views

app_name = 'horoscope'

urlpatterns = [
    path('leo/', views.leo),
    path('scorpion/', views.scorpion),

]