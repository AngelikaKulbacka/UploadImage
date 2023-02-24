from django.db import models
from django.contrib.auth.models import Group, Permission

class UserTier(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name
