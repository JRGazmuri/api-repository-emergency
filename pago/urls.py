from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatosPagoViewSet, BoletaViewSet

router = DefaultRouter()
router.register(r'pagos', DatosPagoViewSet)
router.register(r'boleta', BoletaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
