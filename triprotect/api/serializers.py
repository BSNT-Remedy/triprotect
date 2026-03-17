from rest_framework import serializers

class SensorReadingSerializer(serializers.Serializer):
    device_id = serializers.CharField()
    earthquake = serializers.FloatField()
    fire = serializers.IntegerField()
    electrical = serializers.IntegerField()
