from django.contrib import admin

from .models import IceCream, Image

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image',)
    extra = 1

@admin.register(IceCream)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
    list_filter = ('name', 'quantity')
    search_fields = ('name',)
    list_editable = ('quantity', 'price')
    inlines = [ImageInline]

