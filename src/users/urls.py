from django.contrib.auth import get_user_model
from django.urls import path
from users.api import user_create, user_retrieve, user_update, users_list

User = get_user_model()

urlpatterns = [
    path("", users_list),
    path("", user_create),
    path("<int:id_>/", user_update),
    path("<int:id_>/", user_retrieve),
]
