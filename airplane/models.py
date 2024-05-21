from math import log

from django.db import models


class Airplane(models.Model):
    name = models.CharField(max_length=100)
    passengers = models.IntegerField(default=0)

    def get_fuel_tank_capacity(self) -> int:
        return 200 * self.id

    def get_fuel_consumption(self) -> float:
        return log(self.id * 0.80)

    def get_actual_fuel_consumption(self) -> float:
        return self.get_fuel_consumption() + (self.passengers * 0.002)

    def get_max_flight_minutes(self):
        return (
            self.get_fuel_tank_capacity()
            // self.get_actual_fuel_consumption()
        )
