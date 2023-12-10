from django.urls import path
from .views import index, home

# Tutor
from . views import tutor_cadastrar


urlpatterns = [
    # Login do sistema
    path('', index, name='index'),
    
    # Home do sistemas
    path('home/', home, name='home'),
    
    # Tutores
    path('tutor_cadastrar', tutor_cadastrar, name='tutor_cadastrar')
]