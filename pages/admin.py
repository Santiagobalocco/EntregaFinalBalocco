from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('date', 'author')
    search_fields = ('title', 'subtitle', 'content')
