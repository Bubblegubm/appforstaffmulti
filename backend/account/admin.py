from django.contrib import admin
from .models import Organization, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    raw_id_fields = ['user']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_filter = ['name']