from django.urls import path
from .views import index, home, custom_404

handler404 = custom_404

urlpatterns = [
    # Login do sistema
    path('', index, name='index'),
    
    # Home do sistemas
    path('home/', home, name='home'),
    
    # Erros
]