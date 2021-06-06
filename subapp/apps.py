from django.apps import AppConfig
from django_client_framework.permissions import default_groups, add_perms_shortcut

class SubappConfig(AppConfig):
    name = 'subapp'

    def ready(self):
        pass
        # from .models import Product, Brand
        
        # add_perms_shortcut(default_groups.anyone, Product, "rwcd")
        # add_perms_shortcut(default_groups.anyone, Brand, "rwcd")