from django.contrib import admin
from .models import Movie # Import the Movie model

# Register the Movie model with the Django admin site.
# This allows you to manage Movie objects through the /admin interface.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # 'pass' means no custom admin options are defined yet.
    # You could add list_display, search_fields, list_filter, etc., here if needed.
    pass
