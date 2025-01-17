from django.contrib.auth.models import User as Usuario
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarroSerializer
from .models import Carro
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from inventario.models import Producto

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def agregarProducto(request):
    serializer = CarroSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        carro = Carro.objects.filter(id_usuario=request.user.id)
        carro_serializer = CarroSerializer(carro, many=True)

        productos_con_precios = []
        for item in carro_serializer.data:
            producto_id = item['id_producto']
            producto = Producto.objects.get(id=producto_id)
            item_con_precio = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'cantidad': item['cantidad'],
                'precio_unitario': int(producto.precio),
                'precio_total': int(producto.precio * item['cantidad'])
            }
            productos_con_precios.append(item_con_precio)
        # return Response({'productos_carro': carro_serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'productos_carro': productos_con_precios}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mostrarProducto(request):
    if(request.user.id): 
        carro = Carro.objects.filter(id_usuario=request.user.id)
        carro_serializer = CarroSerializer(carro, many=True)

        productos_con_precios = []
        for item in carro_serializer.data:
            producto_id = item['id_producto']
            producto = Producto.objects.get(id=producto_id)
            item_con_precio = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'cantidad': item['cantidad'],
                'precio_unitario': int(producto.precio),
                'precio_total': int(producto.precio * item['cantidad'])
            }
            productos_con_precios.append(item_con_precio)

        # return Response({'productos_carro': carro_serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'productos_carro': productos_con_precios}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Usuario no registrado'}, status=status.HTTP_200_OK)