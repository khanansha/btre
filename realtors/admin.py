from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorsModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name')

admin.site.register(Realtor, RealtorsModel)
