from django.contrib import admin
from .models import Youtuber
# Register your models here.

class YtAdmin(admin.ModelAdmin):
    list_display=('id','name','is_featured','city')
    list_display_links=('id','name')
    search_fields=('name','city')
    list_filter=('city','crew','category')
    #list_editable=('is_featured','city')

admin.site.register(Youtuber,YtAdmin)
