from django.urls import path
from .views import CalculateDistance, GeolocationView, HistoryData

urlpatterns = [
	path('', GeolocationView.as_view(), name='geolocation'),
	path('api/calculate-distance/', CalculateDistance.as_view(), name='calculate-distance'),
	path('api/history/', HistoryData.as_view(), name='history'),
]
