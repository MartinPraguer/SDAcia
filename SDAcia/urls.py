"""SDAcia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from viewer.models import ZnackyAut, TypKaroserie, Inzeraty, Komentare
from viewer.views import index, hledani, inzeraty, podrobne_hledani, pridat_inzerat, inzeraty_list

admin.site.register(ZnackyAut)
admin.site.register(TypKaroserie)
admin.site.register(Inzeraty)
admin.site.register(Komentare)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("hledani/", hledani),
    path('inzeraty/', inzeraty_list, name='inzeraty_list'),
    path("inzeraty/<int:pk>/", inzeraty, name='inzeraty'),
    path("podrobne_hledani/", podrobne_hledani, name="podrobne_hledani"),
    path('pridat_inzerat/', pridat_inzerat, name='pridat_inzerat'),
]
