from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("auth/", include("authentication.urls")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
