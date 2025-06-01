from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
# from .forms import MovieForm # Mantener comentado si no lo estás usando

def movie_list(request):
    """
    Displays a list of all movies, ordered by title.
    """
    movies = Movie.objects.all().order_by('title')
    context = {
        'movies': movies
    }
    #  El template se busca directamente en 'index.html'
    # Esto asume que el archivo está en 'movies/templates/index.html'
    return render(request, 'index.html', context)

def movie_detail(request, movie_id: int):
    """
    Displays the details of a single movie.
    """
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    #  El template se busca directamente en 'display_movie.html'
    # Esto asume que el archivo está en 'movies/templates/display_movie.html'
    return render(request, 'display_movie.html', context)

# La vista add_movie (o el formulario) si la usas, también cambiaría:
"""
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_list')
    else:
        form = MovieForm()
    # CAMBIO CRÍTICO: El template se busca directamente en 'movie_form.html'
    # Esto asume que el archivo está en 'movies/templates/movie_form.html'
    return render(request, 'movie_form.html', {'form': form})
"""
