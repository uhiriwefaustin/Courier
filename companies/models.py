from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=255)

    def __str__(self):
        return self.name
