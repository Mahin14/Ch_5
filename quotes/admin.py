from django.contrib import admin
from . models import quote
from . models import QuoteCategory


admin.site.register(QuoteCategory)
admin.site.register(quote)



