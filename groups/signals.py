from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import BasicTierPermissions, PremiumTierPermissions, EnterpriseTierPermissions

@receiver(post_save, sender=Group)
def create_group_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.name == "Basic":
            permission = Permission.objects.get(codename="can_view_200px_thumbnail")
            instance.permissions.add(permission)
            BasicTierPermissions.objects.create(group=instance)
        elif instance.name == "Premium":
            permission1 = Permission.objects.get(codename="can_view_200px_thumbnail")
            permission2 = Permission.objects.get(codename="can_view_400px_thumbnail")
            permission3 = Permission.objects.get(codename="can_view_original_image")
            instance.permissions.add(permission1, permission2, permission3)
            PremiumTierPermissions.objects.create(group=instance)
        elif instance.name == "Enterprise":
            permission1 = Permission.objects.get(codename="can_view_200px_thumbnail")
            permission2 = Permission.objects.get(codename="can_view_400px_thumbnail")
            permission3 = Permission.objects.get(codename="can_view_original_image")
            permission4 = Permission.objects.get(codename="can_generate_expiring_link")
            instance.permissions.add(permission1, permission2, permission3, permission4)
            EnterpriseTierPermissions.objects.create(group=instance)
