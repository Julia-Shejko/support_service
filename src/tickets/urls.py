from django.urls import path
from tickets.api import ticket_create, ticket_destroy, ticket_retrieve, ticket_update, tickets_list

urlpatterns = [
    path("", ticket_create),
    path("<int:id_>/", ticket_destroy),
    path("<int:id_>/", ticket_retrieve),
    path("", tickets_list),
    path("<int:id_>/", ticket_update),
]
