from rest_framework import serializers
from .models import ExInterno,ExLaboratorio,DocResInterno,DocResLaboratorio

class ExamenInternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExInterno
        fields = '__all__'

class DocInternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocResInterno
        fields = '__all__'

class ExamenExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExLaboratorio
        fields = '__all__'