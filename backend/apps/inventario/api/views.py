from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Producto
from .serializers import ProductoSerializer, ProductoCreateSerializer
from .filters import ProductoFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductoFilter
    search_fields = ['nombre', 'codigo', 'descripcion']
    ordering_fields = ['nombre', 'precio_venta', 'stock', 'updated_at']
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductoCreateSerializer
        return ProductoSerializer
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Productos con stock bajo"""
        productos = self.get_queryset().filter(stock__lte=5)
        page = self.paginate_queryset(productos)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Estadísticas del inventario"""
        total_products = self.get_queryset().count()
        total_value = sum(p.precio_venta * p.stock for p in self.get_queryset())
        low_stock_count = self.get_queryset().filter(stock__lte=5).count()
        
        return Response({
            'total_products': total_products,
            'total_value': total_value,
            'low_stock_count': low_stock_count,
        })