from rest_framework import serializers
from .models import ExInterno,ExLaboratorio

class ExamenInternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExInterno
        fields = '__all__'

class ExamenExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExLaboratorio
        fields = '__all__'