from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FireInSerializer, EarthquakeInSerializer, ElectricalInSerializer, FireOutSerializer, EarthquakeOutSerializer, ElectricalOutSerializer
from .models import FireReading, EarthquakeReading, ElectricalReading


class FireDataView(APIView):
    
    def get(self, request):
        readings = FireReading.objects.all().order_by('-id')[:100]
        data = FireOutSerializer(readings, many=True).data
        return Response(data, status=200)

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
            source_ts=d.get('timestamp'),
        )
        return Response({'status': 'ok', 'id': obj.id}, status=201)

class EarthquakeDataView(APIView):
    
    def get(self, request):
        readings = EarthquakeReading.objects.all().order_by('-id')[:100]
        data = EarthquakeOutSerializer(readings, many=True).data
        return Response(data, status=200)

    def post(self, request):
        s = EarthquakeInSerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, status=400)
        d = s.validated_data
        obj = EarthquakeReading.objects.create(
            node_id=d['node_id'],
            earthquakeX = d['earthquakeX'],
            earthquakeY = d['earthquakeY'],
            source_ts = d.get('timestamp'),
        )
        return Response({'status': 'ok', 'id': obj.id}, status=201)

class ElectricalDataView(APIView):
    
    def get(self, request):
        readings = ElectricalReading.objects.all().order_by('-id')[:100]
        data = ElectricalOutSerializer(readings, many=True).data
        return Response(data, status=200)

    def post(self, request):
        s = ElectricalInSerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, status=400)
        d = s.validated_data
        obj = ElectricalReading.objects.create(
            node_id=d['node_id'],
                amps = d['amps'],
                source_ts = d.get('timestamp'),
        )
        return Response({'status': 'ok', 'id': obj.id}, status=201)