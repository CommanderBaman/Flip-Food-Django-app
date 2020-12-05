from django.db import models
from django.utils import timezone

# Create your models here.


class DailyValue(models.Model):
    solar_meter_company = models.FloatField()
    solar_meter_actual = models.FloatField()
    consumption = models.FloatField()
    dateRecorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Values recorded are: Generation = {} (Company) {} (Actual), Consumption = {}".format(self.solar_meter_company, self.solar_meter_actual, self.consumption)

    def __repr__(self):
        return "Values recorded are: Generation = {} (Company) {} (Actual), Consumption = {}".format(self.solar_meter_company, self.solar_meter_actual, self.consumption)
