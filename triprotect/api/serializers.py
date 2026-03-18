from rest_framework import serializers
from .models import FireReading, EarthquakeReading, ElectricalReading


class FireInSerializer(serializers.Serializer):
    node_id = serializers.CharField(max_length=64)
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    gas_level = serializers.FloatField()
    timestamp = serializers.DateTimeField(required=False)


class EarthquakeInSerializer(serializers.Serializer):
    node_id = serializers.CharField(max_length=64)
    earthquakeX = serializers.FloatField()
    earthquakeY = serializers.FloatField()
    timestamp = serializers.DateTimeField(required=False)


class ElectricalInSerializer(serializers.Serializer):
    node_id = serializers.CharField(max_length=64)
    amps = serializers.FloatField()
    timestamp = serializers.DateTimeField(required=False)



class FireOutSerializer(serializers.ModelSerializer):
  class Meta:
      model = FireReading
      fields = ["id", "node_id", "temperature", "humidity", "gas_level", "source_ts", "created_at"]

class EarthquakeOutSerializer(serializers.ModelSerializer):
  class Meta:
      model = EarthquakeReading
      fields = ["id", "node_id", "earthquakeX", "earthquakeY", "source_ts", "created_at"]

class ElectricalOutSerializer(serializers.ModelSerializer):
  class Meta:
      model = ElectricalReading
      fields = ["id", "node_id", "amps", "source_ts", "created_at"]
