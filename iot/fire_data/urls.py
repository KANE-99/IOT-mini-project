from django.urls import path
from rest_framework import routers
from .api import DataViewSet

router = routers.DefaultRouter()
router.register('api/data',DataViewSet,'data')
urlpatterns = router.urls
