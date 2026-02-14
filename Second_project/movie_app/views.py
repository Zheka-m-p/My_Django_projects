from django.shortcuts import render, get_object_or_404
from .models import Movie
# функции для выборки, по сути всё как в SQL, + для сотировки (+asc, desc)
from django.db.models import F, Min, Max, Count, Avg

# Create your views here.
def show_all_movie(request):
    movies = Movie.objects.all()
    stats = movies.aggregate(avg_budget=Avg('budget'), max_rating=Max('rating'),
                             min_year=Min('year'), max_year=Max('year'), count_film=Count('id'))
    # movies = Movie.objects.order_by('-rating', 'budget')[:2] # способ сортировки по полям
    context = {
        'movies': movies,
        'stats' : stats
    }
    return render(request, 'movie_app/all_movies.html', context=context)


def one_movie(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    context={
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context)