from rest_framework.routers import DefaultRouter
from .views import ParkViewSet, ParkInfoViewSet

router = DefaultRouter()
router.register('park', ParkViewSet, basename="park-car")
router.register('park_info', ParkInfoViewSet, basename="park-info")