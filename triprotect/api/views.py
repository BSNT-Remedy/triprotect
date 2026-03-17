from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorReadingSerializer
from .models import SensorReading

class SensorDataView(APIView):
    def post(self, request):
        serializer = SensorReadingSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            SensorReading.objects.create(
                device_id=data['device_id'],
                earthquake=data['earthquake'],
                fire=data['fire'],
                electrical=data['electrical']
            )

            return Response({"status": "ok"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)