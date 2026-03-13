from django.db import models
from packages.models import Package
from logistics.models import Station

class Tracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='tracking_history')
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, blank=True)
    current_location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_update = models.CharField(max_length=255)

    def __str__(self):
        return f"Tracking {self.tracking_id} for Package {self.package_id}"

class PackageException(models.Model):
    exception_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='exceptions')
    exception_type = models.CharField(max_length=100)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exception {self.exception_id} - {self.exception_type}"
