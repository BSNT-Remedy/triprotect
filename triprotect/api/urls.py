from django.urls import path
from .views import SensorDataView

urlpatterns = [
    path('sensor/', SensorDataView.as_view(), name='sensor-data'),
]