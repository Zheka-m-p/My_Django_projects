from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def show_all_movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie_app/all_movies.html', context=context)


def one_movie(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    context={
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context)