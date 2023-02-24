from django.db import models
from django.contrib.auth.models import Group, Permission

class BasicTierPermissions(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    can_view_200px_thumbnail = models.BooleanField(default=True)

class PremiumTierPermissions(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    can_view_200px_thumbnail = models.BooleanField(default=True)
    can_view_400px_thumbnail = models.BooleanField(default=True)
    can_view_original_image = models.BooleanField(default=True)

class EnterpriseTierPermissions(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    can_view_200px_thumbnail = models.BooleanField(default=True)
    can_view_400px_thumbnail = models.BooleanField(default=True)
    can_view_original_image = models.BooleanField(default=True)
    can_generate_expiring_link = models.BooleanField(default=True)