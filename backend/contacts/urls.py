from rest_framework.routers import DefaultRouter

from .views import ContactViewSet

router = DefaultRouter()

router.register(
    "",
    ContactViewSet,
    basename="contacts",
)

urlpatterns = router.urls

# /api/v1/contacts/
