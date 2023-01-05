from django.contrib import admin
from .models import Cars, Song, Musician, Award

# Register your models here.

admin.site.register(Cars)
admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Award)
