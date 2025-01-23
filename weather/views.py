from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import WeatherSerializer
import requests

# Create your views here.

class WeatherView(APIView):
    def get(self, request, city):
        api_key = '7b214261317e41c3b81163324252301'
        base_url = 'http://api.weatherapi.com/v1/current.json'
        params = {
            'key': api_key,
            'q': city,
            'aqi': 'yes'
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data  = response.json()
            result = {
                'city': data['location']['name'],
                'temperature': data['current']['temp_c'],
                'description': data['current']['condition']['text']
            }
            serializer = WeatherSerializer(result)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'City not found'}, status=response.status_code)
