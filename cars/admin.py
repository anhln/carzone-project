from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src={} width="40" style="border-radius:50px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'color', 'model', 'year', 'body_style','fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail','car_title')
    search_fields = ( 'car_title', 'model')

admin.site.register(Car, CarAdmin)
