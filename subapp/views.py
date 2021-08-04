from django.http import HttpResponse
from subapp.models import Product, Brand
from subprocess import run
from django_client_framework.permissions import (
    default_groups,
    add_perms_shortcut,
    reset_permissions,
)


def clear(request):
    shell("python3 manage.py flush --no-input")
    reset_permissions()
    add_perms_shortcut(default_groups.anyone, Product, "rwcd")
    add_perms_shortcut(default_groups.anyone, Brand, "rwcd")
    return HttpResponse("Successfully deleted all.")


def shell(cmd, **kwargs):
    print(f"+ {cmd}", flush=True)
    return run(cmd, shell=True, text=True, check=True, **kwargs)
