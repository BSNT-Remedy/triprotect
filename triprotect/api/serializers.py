from rest_framework import serializers


class FireInSerializer(serializers.Serializer):
    """
    Expected payload for /api/fire/ (POST):
    {
      "node_id": "ROOM_1_FIRE",
      "packet_id": 12,
      "temperature": 29.8,
      "humidity": 58.5,
      "gas_level": 352,
      "rssi": -84,                 # optional
      "timestamp": "2026-03-15T09:30:00Z"  # optional (ISO8601)
    }
    """
    node_id = serializers.CharField(max_length=64)
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    gas_level = serializers.FloatField()
    rssi = serializers.IntegerField(required=False)
    timestamp = serializers.DateTimeField(required=False)


class EarthquakeInSerializer(serializers.Serializer):
    """
    Expected payload for /api/earthquake/ (POST):
    {
      "node_id": "HALLWAY_PILLAR",
      "packet_id": 34,
      "earthquakeX": 0.03,
      "earthquakeY": -0.01,
      "rssi": -90,                      # optional
      "timestamp": "2026-03-15T09:31:00Z"  # optional
    }
    """
    node_id = serializers.CharField(max_length=64)
    earthquakeX = serializers.FloatField()
    earthquakeY = serializers.FloatField()
    rssi = serializers.IntegerField(required=False)
    timestamp = serializers.DateTimeField(required=False)


class ElectricalInSerializer(serializers.Serializer):
    """
    Expected payload for /api/electrical/ (POST):
    {
      "node_id": "ROOM_1_ELEC",
      "packet_id": 7,
      "amps": 2.02,
      "rssi": -78,                      # optional
      "timestamp": "2026-03-15T09:32:00Z"  # optional
    }
    """
    node_id = serializers.CharField(max_length=64)
    amps = serializers.FloatField()
    rssi = serializers.IntegerField(required=False)
    timestamp = serializers.DateTimeField(required=False)