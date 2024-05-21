from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from airplane.models import Airplane
from airplane.serializers import (
    AirplaneSerializer,
    AirplaneListSerializer,
    AirplaneDetailSerializer
)


class AirplaneViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneListSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return AirplaneSerializer
        if self.action == "retrieve":
            return AirplaneDetailSerializer

        return self.serializer_class
