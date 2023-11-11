from rest_framework import serializers
from attractions.models import *


class AttractionSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)

    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'address', 'musculoskeletal_disorders', 'visual_impairment', 'hearing_impairment', 'intellectual_impairment', 'lat', 'lon', 'cover')