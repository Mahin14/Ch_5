from django.contrib import admin

from . models import Joke_catagory
from . models import joke

admin.site.register(Joke_catagory)
admin.site.register(joke)
