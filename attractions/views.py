import json
import requests
from attractions.models import *
from attractions.serializers import *
from users.permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile



class AttractionAPIListCreate(generics.ListCreateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    permission_classes = [IsAdminOrReadOnly]


@api_view(['POST'])
def generate_attraction(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', None)
        description = data.get('description', None)
        address = data.get('address', None)
        cover = data.get('cover', None)
        category = data.get('category', None)
        lat = data.get('lat', None)
        lon = data.get('lon', None)

        if not Attraction.objects.filter(name=name).exists():
            attraction = Attraction(name=name, description=description, address=address, category=category,
                                    lat=lat, lon=lon)

            if cover:
                image = requests.get(cover)
                image_data = ContentFile(image.content)
                image_name = str(uuid.uuid4())
                attraction.cover.save(f'{image_name}.png', image_data, save=True)

            attraction.save()

        return Response({'message': 'Attraction was generated', 'data': request.data})