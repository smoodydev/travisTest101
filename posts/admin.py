from django.contrib import admin
from .models import Post

# Register your models here.

# And we're going to just register our Post class with our admin site.
admin.site.register(Post)
