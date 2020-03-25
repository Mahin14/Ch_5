from django.views.generic import ListView
from . models import joke
from . models import Joke_catagory



# Create your views here.
class HomeView(ListView):
    template_name="index.html"
    model=joke
    def get_queryset(self):
        query_set =super().get_queryset()
        return query_set.select_related
        ('quote_category')
