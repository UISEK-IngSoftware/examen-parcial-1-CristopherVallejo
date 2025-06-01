from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, null=False)
    genre = models.CharField(max_length=100, null=False)
    director_name = models.CharField(max_length=200, null=False)
    publication_year = models.IntegerField(null=False)
    synopsis = models.TextField(null=False)
    # Campo para la imagen de la película
    # Las imágenes se guardarán en la carpeta 'movie_posters' dentro de MEDIA_ROOT
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    class Meta:
        ordering = ['title']
