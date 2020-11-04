from django.contrib import admin

from .models import User, Agent, UserProfile


class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name']
    list_display_links = ['id', 'username']
    list_filter = ['username', 'email', 'phone_number']
    search_fields = ['username', 'email', 'phone_number']
    list_per_page = 8


admin.site.register(User, AdminUser)


class AgentAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'agent', 'company_name']
    list_editable = ['contact_number', 'website']
    list_display = ['id', 'agent', 'company_name', 'website', 'contact_number']


admin.site.register(Agent, AgentAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'created_at', 'updated_at']
    search_fields = ['user', 'address']
    list_filter = ['user', 'address']
    list_per_page = 8


admin.site.register(UserProfile, ProfileAdmin)
