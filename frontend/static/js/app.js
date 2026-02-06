// Módulo principal de la aplicación
import ApiClient from './lib/api-client.js';
import AuthManager from './lib/auth-manager.js';
import Notification from './components/notification.js';
import ProductTable from './components/product-table.js';

class App {
    constructor() {
        this.api = new ApiClient(window.APP_CONFIG.api.baseUrl);
        this.auth = new AuthManager(this.api);
        this.notifications = new Notification();
        this.components = new Map();
        
        this.init();
    }
    
    async init() {
        // Verificar autenticación
        if (!await this.auth.checkAuth()) {
            this.redirectToLogin();
            return;
        }
        
        // Inicializar componentes según la página
        this.initPageComponents();
        
        // Configurar interceptores globales
        this.setupInterceptors();
    }
    
    initPageComponents() {
        // Tabla de productos (si existe en la página)
        const productTableEl = document.getElementById('product-table');
        if (productTableEl) {
            const productTable = new ProductTable(productTableEl, {
                api: this.api,
                onDelete: this.handleProductDelete.bind(this)
            });
            this.components.set('productTable', productTable);
        }
        
        // Formularios
        document.querySelectorAll('[data-form]').forEach(formEl => {
            // Inicializar formularios dinámicos
        });
    }
    
    setupInterceptors() {
        // Interceptor para manejar errores 401
        this.api.addInterceptor({
            onError: (error) => {
                if (error.status === 401) {
                    this.auth.logout();
                    this.redirectToLogin();
                }
                throw error;
            }
        });
    }
    
    redirectToLogin() {
        window.location.href = '/login/';
    }
    
    handleProductDelete(product) {
        this.notifications.confirm(
            `¿Eliminar ${product.nombre}?`,
            'Esta acción no se puede deshacer',
            async () => {
                try {
                    await this.api.delete(`/products/${product.id}/`);
                    this.notifications.success('Producto eliminado');
                    this.components.get('productTable')?.refresh();
                } catch (error) {
                    this.notifications.error('Error al eliminar producto');
                }
            }
        );
    }
}

// Inicializar aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});