"""dart_test_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import django_client_framework.api.urls
from django_client_framework.permissions import default_groups, add_perms_shortcut
from subapp.models import Product
from subapp.models import Brand
from subapp import urls as subappurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(django_client_framework.api.urls)),
    path('subapp/', include(subappurls))
]

add_perms_shortcut(default_groups.anyone, Product, "rwcd")
add_perms_shortcut(default_groups.anyone, Brand, "rwcd")