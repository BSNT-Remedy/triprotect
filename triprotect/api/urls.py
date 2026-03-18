from django.urls import path
from .views import FireDataView, EarthquakeDataView, ElectricalDataView

urlpatterns = [
    path('fire/', FireDataView.as_view(), name='fire-data'),
    path('earthquake/', EarthquakeDataView.as_view(), name='earthquake-data'),
    path('electrical/', ElectricalDataView.as_view(), name='electrical-data'),
]