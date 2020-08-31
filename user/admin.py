from django.contrib import admin

from .models import User, Agent


class AdminUser(admin.ModelAdmin):
    list_display = ['_id', 'username', 'email', 'phone_number', 'first_name', 'last_name']
    list_display_links = ['_id', 'username']
    list_filter = ['username', 'email', 'phone_number']
    search_fields = ['username', 'email', 'phone_number']
    list_per_page = 8


admin.site.register(User, AdminUser)


class AgentAdmin(admin.ModelAdmin):
    list_display = ['agent', 'company_name', 'website']


admin.site.register(Agent, AgentAdmin)
