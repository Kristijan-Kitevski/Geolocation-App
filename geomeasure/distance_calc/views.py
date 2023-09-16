import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import combinations
from geopy.distance import great_circle
from geomeasure.settings import GEOCODING_KEY
from django.shortcuts import render
from .models import DistanceCalculation


class GeolocationView(APIView):
	def get(self, request):
		return render(request, 'geolocation_template.html')


class CalculateDistance(APIView):
	def post(self, request, format=None):
		places_data = request.data
		place_coordinates = []

		for place_info in places_data:
			place_name = place_info.get('place')
			if place_name:
				place_name = place_name.replace(' ', '+')
				api_key = GEOCODING_KEY

				# Example using Google Maps Geocoding API
				api_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={api_key}'

				response = requests.get(api_url)
				if response.status_code == 200:
					data = response.json()
					if data.get('results'):
						result = data['results'][0]
						location = result['geometry']['location']
						latitude = location['lat']
						longitude = location['lng']
						place_coordinates.append({
							'place': place_info['place'],
							'latitude': latitude,
							'longitude': longitude
						})
					else:
						return Response({'message': 'Geocoding failed for some place(s)'}, status=status.HTTP_400_BAD_REQUEST)
				else:
					return Response({'message': 'Geocoding API request failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			else:
				return Response({'message': 'Invalid place name(s)'}, status=status.HTTP_400_BAD_REQUEST)

		distances = []
		for place1, place2 in combinations(place_coordinates, 2):
			distance = great_circle(
				(place1['latitude'], place1['longitude']),
				(place2['latitude'], place2['longitude'])
			).kilometers
			distances.append({
				'place1': place1['place'],
				'place2': place2['place'],
				'distance': round(distance, 2)
			})

			# Save the calculation in the database
			DistanceCalculation.objects.create(
				place1=place1['place'],
				place2=place2['place'],
				distance=distance
			)

		return Response(distances)


class HistoryData(APIView):
	def get(self, request, format=None):
		try:
			last_input = DistanceCalculation.objects.last()	
		except:	
			return Response({'message': 'No history'}, status=status.HTTP_400_BAD_REQUEST)
		data = []
		data.append({
			'place1': last_input.place1,
			'place2': last_input.place2,
			'distance': last_input.distance
		})

		return Response(data)
