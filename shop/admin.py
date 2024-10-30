from django.contrib import admin
from .models import Collection, Product  # Changed from Category to Collection

@admin.register(Collection)  # Changed from Category to Collection
class CollectionAdmin(admin.ModelAdmin):  # Changed from CategoryAdmin to CollectionAdmin
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'quantity', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'quantity', 'available']
    prepopulated_fields = {'slug': ('name',)}
