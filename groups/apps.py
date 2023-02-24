from django.apps import AppConfig
import django.utils.translation


class GroupsConfig(AppConfig):
    name = 'groups'
    verbose_name = django.utils.translation.gettext_lazy('groups')

    def ready(self):
        import groups.signals