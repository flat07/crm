from rest_framework.routers import DefaultRouter

from .views import DealViewSet

router = DefaultRouter()

router.register(
    "",
    DealViewSet,
    basename="deals",
)

urlpatterns = router.urls

# /api/v1/deals/
