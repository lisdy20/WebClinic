from rest_framework import serializers
from .models import ExInterno

class ExamenInternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExInterno
        fields = '__all__'