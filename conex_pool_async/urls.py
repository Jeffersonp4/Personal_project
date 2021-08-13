"""conex_pool_async URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from class_date.views import details_conex, Add_connex
from pool_view.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida, name='Index'),
    path('details_connex/<int:id>', details_conex),
    path('Add_connex', Add_connex)
]