from math import log

from django.db import models


class Airplane(models.Model):
    name = models.CharField(max_length=100, nullable=False)
    passengers = models.IntegerField(default=0)

    def get_fuel_tank_capacity(self):
        return 200 * self.id

    def get_fuel_consumption(self):
        return log(self.id) * 0.80

    def get_actual_fuel_consumption(self):
        return self.get_fuel_consumption() + (self.passengers * 0.002)
