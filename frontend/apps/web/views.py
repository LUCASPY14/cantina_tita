from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.conf import settings

def index(request):
    """Vista principal del frontend"""
    return render(request, 'index.html', {
        'APP_NAME': 'Cantina Tita'
    })

@method_decorator(never_cache, name='dispatch')
class BaseView(TemplateView):
    """Vista base para todas las páginas"""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['API_BASE_URL'] = getattr(settings, 'API_BASE_URL', 'http://localhost:8000')
        context['APP_NAME'] = 'Cantina Tita'
        context['USER'] = self.request.user if self.request.user.is_authenticated else None
        return context

class InventarioView(BaseView):
    template_name = 'inventario/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí podrías hacer fetch a la API si necesitas datos iniciales
        # Pero mejor hacerlo desde el frontend con JavaScript
        return context

class ProductDetailView(BaseView):
    template_name = 'inventario/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = kwargs.get('product_id')
        return context