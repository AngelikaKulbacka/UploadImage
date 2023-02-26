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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        user_tier = form.cleaned_data.get('user_tier')

        if user_tier:
            obj.user_tier = user_tier
            obj.save()
