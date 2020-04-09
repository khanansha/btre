from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingsModel(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'is_published', 'address', 'price', 'bedrooms', 'bathrooms', 'zipcode', 'list_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('realtor',)
    list_per_page = 25
    search_fields = ('title', 'description', 'address', 'price', 'zipcode', 'list_date', 'city', 'state')

admin.site.register(Listing, ListingsModel)