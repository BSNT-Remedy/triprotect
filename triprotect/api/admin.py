from django.contrib import admin
from .models import FireReading, EarthquakeReading, ElectricalReading

admin.site.register(FireReading)
admin.site.register(EarthquakeReading)
admin.site.register(ElectricalReading)