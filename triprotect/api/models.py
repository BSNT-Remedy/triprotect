from django.db import models


class FireReading(models.Model):
    node_id = models.CharField(max_length=64)

    temperature = models.FloatField()
    humidity = models.FloatField()
    gas_level = models.FloatField()

    source_ts = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['node_id', 'created_at']),
        ]

    def __str__(self):
        return f"[FIRE] {self.node_id} @ {self.created_at:%Y-%m-%d %H:%M:%S}"


class EarthquakeReading(models.Model):
    node_id = models.CharField(max_length=64)

    earthquakeX = models.FloatField()
    earthquakeY = models.FloatField()

    source_ts = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['node_id', 'created_at']),
        ]

    def __str__(self):
        return f"[QUAKE] {self.node_id} @ {self.created_at:%Y-%m-%d %H:%M:%S}"


class ElectricalReading(models.Model):
    node_id = models.CharField(max_length=64)

    amps = models.FloatField()

    source_ts = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['node_id', 'created_at']),
        ]

    def __str__(self):
        return f"[ELEC] {self.node_id} @ {self.created_at:%Y-%m-%d %H:%M:%S}"