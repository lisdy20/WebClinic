from rest_framework import serializers
from .models import ControlPago

class ControlPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPago
        fields = '__all__'