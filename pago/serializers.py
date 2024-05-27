from rest_framework import serializers
from .models import DatosPago, Boleta

class DatosPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPago
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    datos_pago = DatosPagoSerializer(many=True, read_only=True)  # Asumiendo que puede haber múltiples pagos asociados a una boleta

    class Meta:
        model = Boleta
        fields = '__all__'