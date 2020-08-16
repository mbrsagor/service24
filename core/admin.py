from django.contrib import admin
from core.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'order_by', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_editable = ['order_by']
    search_fields = ['name', 'order_by']
    list_filter = ['name', 'parent', 'order_by']
    list_per_page = 8


admin.site.register(Category, CategoryAdmin)
