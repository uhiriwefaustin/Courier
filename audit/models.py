from django.db import models

class AuditLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    record_id = models.IntegerField()
    action = models.CharField(max_length=50)
    performed_by = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on {self.table_name} at {self.timestamp}"
