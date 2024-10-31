from rest_framework import serializers
from .models import Paciente,Antecedente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class AntecedenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antecedente
        fields = '__all__'