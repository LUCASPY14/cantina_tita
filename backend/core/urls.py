from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import json

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cantina Tita - Sistema de Gestión</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 40px; max-width: 800px; margin: 0 auto; }
            h1 { color: #2c3e50; }
            .card { background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0; }
            a { color: #3498db; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .success { color: #27ae60; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🎉 ¡Cantina Tita está funcionando!</h1>
        <div class="card">
            <h2>✅ Backend Django corriendo correctamente</h2>
            <p>Servicios activos:</p>
            <ul>
                <li><a href="/admin/" target="_blank">🔧 Admin Django</a> (admin/admin123)</li>
                <li><a href="http://localhost:3000" target="_blank">🎨 Frontend</a> (Django)</li>
                <li><span class="success">🗄️ MySQL:</span> localhost:3307</li>
            </ul>
        </div>
        <p>Proyecto listo para desarrollo.</p>
    </body>
    </html>
    """, content_type="text/html")

def api_root(request):
    response = {
        "status": "running",
        "service": "Cantina Tita API",
        "version": "1.0",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/",
            "home": "/"
        }
    }
    return HttpResponse(json.dumps(response, indent=2), content_type="application/json")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', api_root, name='api-root'),
]
