from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from mailing import views

import mailing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mailing.views.home, name="home"),
    #path('mailing/', include(("mailing.urls", "mailing"), namespace = 'mailing')),
    path('mailing/', include("mailing.urls", namespace="mailing"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


