from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django import forms
from Project.models import UserTier

class UserTierChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class GroupAdminForm(forms.ModelForm):
    user_tier = UserTierChoiceField(queryset=UserTier.objects.all())

    class Meta:
        model = Group
        fields = '__all__'

class CustomGroupAdmin(GroupAdmin):
    form = GroupAdminForm

