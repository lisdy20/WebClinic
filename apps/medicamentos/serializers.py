from rest_framework import serializers
from .models import Medicamento,RecetaMedica,DetalleRecetaMe

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class RecetaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaMedica
        fields = '__all__'

class DetalleRecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleRecetaMe
        fields = '__all__'