from django.views.generic import ListView
from . models import quote
from . models import QuoteCategory


class HomeView(ListView):
    template_name='home.html'
    model= quote

    def get_queryset(self):
        query_set =super().get_queryset()
        return query_set.select_related
        ('quote_category')