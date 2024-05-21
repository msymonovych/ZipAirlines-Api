from django.urls import path, include
from rest_framework import routers

from airplane.views import AirplaneViewSet


router = routers.DefaultRouter()
router.register("airplane", AirplaneViewSet)


urlpatterns = [path("", include(router.urls))]

app_name = 'airplane'
