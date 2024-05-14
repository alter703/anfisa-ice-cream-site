from django.contrib import admin

from .models import FeedBack

# Register your models here.
@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    list_display_links = ('author',)
    list_filter = ('created_at',)