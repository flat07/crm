# backend/contacts/urls.py
from rest_framework.routers import DefaultRouter

from .views import (
    ContactEmailViewSet,
    ContactPhoneViewSet,
    ContactTagAssignmentViewSet,
    ContactTagViewSet,
    ContactViewSet,
)

router = DefaultRouter()


# Remove the trailing slashes inside the register method
router.register("tags", ContactTagViewSet, basename="contact-tags")
router.register("email", ContactEmailViewSet, basename="contact-email")
router.register(
    "assignments", ContactTagAssignmentViewSet, basename="contact-assignments"
)
router.register("phone", ContactPhoneViewSet, basename="contact-phone")
router.register("", ContactViewSet, basename="contacts")

urlpatterns = router.urls

# /api/v1/contacts/
# /api/v1/contacts/tags/
# /api/v1/contacts/phone/
# /api/v1/contacts/email/
