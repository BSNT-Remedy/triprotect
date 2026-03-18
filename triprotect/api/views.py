from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from .serializers import FireInSerializer, EarthquakeInSerializer, ElectricalInSerializer
from .models import FireReading, EarthquakeReading, ElectricalReading

def _parse_ts(ts):
    if not ts:
        return None
    if isinstance(ts, str):
        dt = parse_datetime(ts)
        if dt and dt.tzinfo is None:
            dt = make_aware(dt)
        return dt
    return None

class FireDataView(APIView):
    def post(self, request):
        s = FireInSerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, status=400)
        d = s.validated_data
        obj = FireReading.objects.create(
            node_id=d['node_id'],
            temperature=d['temperature'],
            humidity=d['humidity'],
            gas_level=d['gas_level'],
            rssi=d.get('rssi'),
            source_ts=_parse_ts(d.get('timestamp')),
        )
        return Response({'status': 'ok', 'id': obj.id}, status=201)

class EarthquakeDataView(APIView):
    def post(self, request):
        s = EarthquakeInSerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, status=400)
        d = s.validated_data
        obj = EarthquakeReading.objects.create(
            node_id=d['node_id'],
            earthquakeX = d['earthquakeX'],
            earthquakeY = d['earthquakeY'],
            rssi = d.get('rssi'),
            source_ts = _parse_ts(d.get('timestamp')),
        )
        return Response({'status': 'ok', 'id': obj.id}, status=201)

class ElectricalDataView(APIView):
    def post(self, request):
        s = ElectricalInSerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, status=400)
        d = s.validated_data
        obj = ElectricalReading.objects.create(
            node_id=d['node_id'],
                amps = d['amps'],
                rssi = d.get('rssi'),
                source_ts = _parse_ts(d.get('timestamp')),
        )
        return Response({'status': 'ok', 'id': obj.id}, status=201)