from django.db import models
from companies.models import Company

class BusRoute(models.Model):
    route_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='routes')
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    duration = models.CharField(max_length=50) # e.g., '3 hours'
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.departure_city} to {self.arrival_city}"

class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='stations')
    station_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.station_name} ({self.city})"

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='drivers')

    def __str__(self):
        return self.name
