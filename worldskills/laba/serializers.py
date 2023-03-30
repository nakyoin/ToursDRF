from rest_framework import serializers
from .models import *

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'

class ExcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excourses
        fields = '__all__'