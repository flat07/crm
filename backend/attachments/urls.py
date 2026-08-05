from rest_framework.routers import DefaultRouter

from .views import AttachmentViewSet

router = DefaultRouter()

router.register(
    "",
    AttachmentViewSet,
    basename="attachments",
)

urlpatterns = router.urls

# /api/v1/attachments/
