from django.contrib import admin
from .models import UserTier
from django.contrib.auth.models import Group
from django.contrib import admin
from groups.admin import CustomGroupAdmin


@admin.register(UserTier)
class UserTierAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
