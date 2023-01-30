from authentication.api import _TokenObtainPairView, _TokenRefreshView
from django.urls import path

urlpatterns = [
    path("token/", _TokenObtainPairView.as_view()),
    path("token/refresh/", _TokenRefreshView.as_view()),
]
