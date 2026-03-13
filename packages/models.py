from django.db import models
from clients.models import Client, Receiver
from companies.models import Company
from logistics.models import BusRoute, Driver

class PackageType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type_name

class Package(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Exception', 'Exception'),
    )

    package_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sent_packages')
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE, related_name='received_packages')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='packages')
    route = models.ForeignKey(BusRoute, on_delete=models.SET_NULL, null=True, blank=True, related_name='packages')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='packages')
    package_type = models.ForeignKey(PackageType, on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2) # in kg
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_sent = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Package #{self.package_id} - {self.status}"
