from django.apps import AppConfig

class SubappConfig(AppConfig):
    name = 'subapp'

    def ready(self):
        from django_client_framework.permissions import reset_permissions
        reset_permissions()