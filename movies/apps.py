from django.apps import AppConfig

# Define the AppConfig for the 'movies' application
class MoviesConfig(AppConfig):
    
    default_auto_field = 'django.db.models.BigAutoField'
    
    
    name = 'movies'
