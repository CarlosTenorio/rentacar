from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Country, City
from api.serializers import CitySerializer, CountrySerializer

#########################################
# LOCATIONS VIEW (Countries & Cities)
########################################


class LocationViewSet(viewsets.ViewSet):

    def list(self, request):
        """
        GET (ALL)
        """
        cities_db = City.objects.all()
        # countries_db = Country.objects.all()

        cities_serializer = CitySerializer(cities_db, many=True)
        # countries_serializer = CountrySerializer(countries_db, many=True)

        # locations = cities_serializer.data + countries_serializer.data
        locations = cities_serializer.data

        return Response(locations)
