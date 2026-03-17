from django.db import models

class SensorReading(models.Model):
    device_id = models.CharField(max_length=64)
    earthquake = models.FloatField()
    fire = models.IntegerField()
    electrical = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']