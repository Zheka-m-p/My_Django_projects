from django.urls import path
from . import views

app_name = 'movie' # чисто название, может быть любым, для удобства навигации по url-ам

urlpatterns = [
    path('', views.movie_app_home_page, name='movie_app_home_page'),

    path('all_movies/', views.show_all_movies, name='all_movies'),
    path('all_producers/', views.show_all_producers, name='all_producers'),
    path('all_actors/', views.show_all_actors, name='all_actors'),

    path('movie/<int:id>/', views.one_movie, name='solo_movie'),
    path('producer/<int:id>/', views.one_producer, name='solo_producer'),
    path('actor/<int:id>/', views.one_actor, name='solo_actor'),

]
