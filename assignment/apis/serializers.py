from rest_framework import serializers
from .models import Work, Artist

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['Link', 'Work_type']

class ArtistSerializer(serializers.ModelSerializer):
    Arwork = WorkSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['Arname', 'Arwork']
