from django.urls import path
from . import views

# Define the app_name for namespacing URLs, consistent with the movie catalog theme
app_name = "movies"

# Define URL patterns for the movies application
urlpatterns = [
    # Path for the list of all movies (e.g., http://localhost:8000/ if included at project root)
    # This maps to the movie_list view function
    path("", views.movie_list, name="movie_list"),

    # Path for the detail view of a specific movie by its ID (e.g., http://localhost:8000/1/)
    # This maps to the movie_detail view function
    path("<int:movie_id>/", views.movie_detail, name="movie_detail"),

]
