from django.contrib import admin
from core.models.category import Category
from core.models.location import Location

admin.site.site_header = "Service24"
admin.site.index_title = "Service24 Admin Panel"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'order_by', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_editable = ['order_by']
    search_fields = ['name', 'order_by']
    list_filter = ['name', 'parent', 'order_by']
    list_per_page = 8


admin.site.register(Category, CategoryAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'created_at', 'updated_at']
    list_display_links = ['name']
    search_fields = ['name', 'is_active']
    list_filter = ['name', 'parent', 'is_active']
    list_per_page = 8


admin.site.register(Location, LocationAdmin)
