from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))


    list_display=('id','myphoto','first_name','role')
    list_display_links=('id','first_name')
    search_fields=('role',)
    list_filter=('role',)
# Register your models here.

admin.site.register(Team,TeamAdmin)
admin.site.register(Slider)