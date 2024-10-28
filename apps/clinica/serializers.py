from rest_framework import serializers
from .models import Servicio,Cita,DetalleCita

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class DetalleCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCita
        fields = '__all__'