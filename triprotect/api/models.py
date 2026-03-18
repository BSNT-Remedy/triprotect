from django.db import models


class FireReading(models.Model):
    """
    One row per fire-related reading (temperature/humidity/gas).
    Identified by (node_id, packet_id) to avoid duplicates on retries.
    """
    node_id = models.CharField(max_length=64)

    temperature = models.FloatField()
    humidity = models.FloatField()
    gas_level = models.FloatField()

    rssi = models.IntegerField(null=True, blank=True)
    source_ts = models.DateTimeField(null=True, blank=True)  # gateway/device timestamp (optional)
    created_at = models.DateTimeField(auto_now_add=True)     # server ingest time

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['node_id', 'created_at']),
        ]

    def __str__(self):
        return f"[FIRE] {self.node_id} @ {self.created_at:%Y-%m-%d %H:%M:%S}"


class EarthquakeReading(models.Model):
    """
    One row per earthquake reading (2-axis accel/derived).
    """
    node_id = models.CharField(max_length=64)

    earthquakeX = models.FloatField()
    earthquakeY = models.FloatField()

    rssi = models.IntegerField(null=True, blank=True)
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
    """
    One row per electrical reading (current in amps).
    """
    node_id = models.CharField(max_length=64)

    amps = models.FloatField()

    rssi = models.IntegerField(null=True, blank=True)
    source_ts = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['node_id', 'created_at']),
        ]

    def __str__(self):
        return f"[ELEC] {self.node_id} @ {self.created_at:%Y-%m-%d %H:%M:%S}"