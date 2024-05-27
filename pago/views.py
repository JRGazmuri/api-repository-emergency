from rest_framework import viewsets
from .models import DatosPago, Boleta
from .serializers import DatosPagoSerializer, BoletaSerializer


class BoletaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DatosPagoViewSet(viewsets.ModelViewSet):
    queryset = DatosPago.objects.all()
    serializer_class = DatosPagoSerializer
    