from rest_framework.routers import DefaultRouter
from tickets.api import TicketAPISet

router = DefaultRouter()
router.register("", TicketAPISet, basename="tickets")
urlpatterns = router.urls
