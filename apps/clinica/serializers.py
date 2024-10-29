from rest_framework import serializers
from .models import Servicio,Cita,DetalleCita,Historial

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

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = '__all__'