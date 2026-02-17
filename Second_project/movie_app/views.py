from django.shortcuts import render, get_object_or_404
from .models import Movie, Producer, Actor
# функции для выборки, по сути всё как в SQL, + для сотировки (+asc, desc)
from django.db.models import F, Min, Max, Count, Avg

# Create your views here.
def movie_app_home_page(request):
    return render(request, 'movie_app/movie_app_home_page.html')


def show_all_movies(request):
    movies = Movie.objects.all()
    stats = movies.aggregate(avg_budget=Avg('budget'), max_rating=Max('rating'),
                             min_year=Min('year'), max_year=Max('year'), count_film=Count('id'))
    # movies = Movie.objects.order_by('-rating', 'budget')[:2] # способ сортировки по полям
    context = {
        'movies': movies,
        'stats' : stats,
    }
    return render(request, 'movie_app/all_movies.html', context=context)


def show_all_producers(requrst):
    producers = Producer.objects.all()
    context = {
        'producers': producers,
    }
    return render(requrst, 'movie_app/all_producers.html', context)


def show_all_actors(requrst):
    actors = Actor.objects.all()
    context = {
        'actors': actors,
    }
    return render(requrst, 'movie_app/all_actors.html', context)



def one_movie(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    context={
        'movie': movie,
        'actors': movie.actors, # можно так обращаться к списку актеров
    }
    return render(request, 'movie_app/one_movie.html', context)


def one_producer(request, id):
    producer = get_object_or_404(Producer, id=id)
    movies = producer.movie_set.all()
    context={
        'producer': producer,
        'movies': movies,
    }
    return render(request, 'movie_app/one_producer.html', context)


def one_actor(request, id):
    actor = get_object_or_404(Actor, id=id)
    # movies = actor.movie_set.all() # не повезло, не прокатило)
    movies = Movie.objects.filter(actors=actor)  # еще вариант так
    context={
        'actor': actor,
        'movies': movies,
    }
    return render(request, 'movie_app/one_actor.html', context)


