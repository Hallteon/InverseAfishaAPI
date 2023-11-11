from attractions.models import *
from django.contrib import admin


class AttractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address', 'category', 'musculoskeletal_disorders', 'visual_impairment', 'hearing_impairment', 'intellectual_impairment', 'lat', 'lon', 'cover')
    search_fields = ('id', 'name', 'address')
    list_filter = ('name', 'address')


admin.site.register(Attraction, AttractionAdmin)