from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.apps.inventario.api import views as inventario_views

router = DefaultRouter()
router.register(r'products', inventario_views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('stats/dashboard/', inventario_views.DashboardStatsAPI.as_view(), name='dashboard-stats'),
]