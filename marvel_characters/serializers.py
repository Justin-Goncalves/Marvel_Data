from rest_framework import serializers
from .models import CharacterProfile

class CharacterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterProfile
        fields = '__all__'