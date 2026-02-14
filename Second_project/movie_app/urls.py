from django.urls import path
from . import views

app_name = 'movie' # чисто название, может быть любым, для удобства навигации по url-ам

urlpatterns = [
    path('', views.show_all_movie, name='all_movies'),
    path('movie/<int:id>/', views.one_movie, name='solo_movie'),

]
