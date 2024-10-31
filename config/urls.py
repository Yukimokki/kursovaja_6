from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("mailing.urls")),
    #path('mailing/', include("mailing.urls", namespace="mailing"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


