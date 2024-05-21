from typing import Any, Dict

from rest_framework import serializers

from airplane.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]) -> Airplane:
        max_airplane = 10
        if Airplane.objects.count() >= max_airplane:
            raise serializers.ValidationError(
                "Cannot create more airplanes. Limit reached."
            )
        return super().create(validated_data)


class AirplaneListSerializer(AirplaneSerializer):
    ...


class AirplaneDetailSerializer(AirplaneSerializer):
    fuel_tank_capacity = serializers.IntegerField(
        source="get_fuel_tank_capacity", read_only=True
    )
    fuel_consumption = serializers.FloatField(
        source="get_fuel_consumption", read_only=True
    )
    actual_fuel_consumption = serializers.FloatField(
        source="get_actual_fuel_consumption", read_only=True
    )
    max_flight_minutes = serializers.IntegerField(
        source="get_max_flight_minutes", read_only=True
    )

    class Meta:
        model = Airplane
        fields = [
            "id",
            "name",
            "passengers",
            "fuel_tank_capacity",
            "fuel_consumption",
            "actual_fuel_consumption",
            "max_flight_minutes",
        ]
